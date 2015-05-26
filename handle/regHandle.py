# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import json
import random
import urllib

import tornado
from tornado.web import authenticated;

from tornado import gen
import tornado.httpclient

from error.zebraError import ZebraError
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class RegHandler(BaseHandler):
    # @tornado.web.asynchronous
    def back(self):
        yield tornado.gen.Task(self.reg)
        self.finish()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        result = ""
        try:
            username = self.get_argument("un")
            password = self.get_arguments("pw")
            retryPassword = self.get_arguments("rpw")
            mcode1 = self.get_argument("mcode")
            mcode2 = self.session["mcode"]

            if mcode2 is not None and mcode1 == mcode2:
                if password == retryPassword:
                    rcds = self.userService.getByUsername(username)
                    if (len(rcds)) == 0:
                        res = self.userService.add({"username": username, "password": password})
                        result = JsonTemplate.newJsonRes().toJson()
                    else:
                        result = JsonTemplate.newErrorJsonRes().setErrMsg("用户名已存在或格式不正确").toJson()
                else:
                    result = JsonTemplate.newErrorJsonRes().setErrMsg("密码不相同或格式不正确").toJson()
            else:
                result = JsonTemplate.newErrorJsonRes().setErrMsg("验证码不正确或没有验证码").toJson()
        except ZebraError as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e).toJson()
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg("unknow error").toJson()
        finally:
            raise gen.Return(result)

class SendPhoneCodeHandle(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        result = JsonTemplate.newJsonRes().setErrMsg("success").toJson()
        try:
            key = "a899cda8e885b07a7b4615011780d2a4"
            phone = self.get_argument("ph")
            template = "3030"
            code = random.randrange(100000, 999999)
            client = tornado.httpclient.AsyncHTTPClient()
            args = urllib.urlencode(
                {'mobile': phone, 'tpl_id': template, 'tpl_value': "#code#=%s" % (code), 'key': key})

            url = "http://v.juhe.cn/sms/send?%s" % args
            resp = yield client.fetch(url)
            body = json.loads(resp.body)
            if (body["error_code"] > 0):
                print body
                result = JsonTemplate.newErrorJsonRes().setErrMsg("call api failed").toJson()
            else:
                self.session["mcode"] = '%s' % code
                self.session.save();

        except Exception as e:
            print e
            result = JsonTemplate.newErrorJsonRes().setErrMsg("unknow error").toJson()
        finally:
            self.write(result)
            self.finish()
            pass