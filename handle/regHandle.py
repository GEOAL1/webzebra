# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import base64
import json
import random

import tornado
import tornado.httpclient

from tornado.web import authenticated;

from tornado import gen

from error.zebraError import *
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID
from utils.messageUtils import MessageUtile


class RegHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        result = ""
        try:
            phone, password = self.argCheck()

            self.userService.getByPhone(phone)

            res = self.userService.add({"phone": phone, "password": password})

            if res is None:
                raise RegInerError()

            result = JsonTemplate.newJsonRes()
            self.session[SessionUserID] = res["id"]
            self.session.save();

        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())

    def argCheck(self):
        try:
            password = self.get_argument("password")
            retryPassword = self.get_argument("confirmPassword")
            phone = self.get_argument("ph")
            # mcode1 = self.get_argument("confirmCode")
            # mcode2 = self.session["confirmCode"]
            mcode1 = 123456;
            mcode2 = 123456;
        except:
            raise InputArgsError()

        if mcode2 is None or mcode1 != mcode2:
            raise ValidateCodeError()

        if password != retryPassword:
            raise SamePasswordError()
        phone = base64.decodestring(phone)
        return phone, password

class SendPhoneCodeHandle(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    def get_result(self):
        try:
            try:
                phone = self.get_argument("ph")
            except Exception as e:
                raise InputArgsError()
            code = random.randrange(100000, 999999)
            code = 123456
            resp = MessageUtile.sendValidCode(phone, code)
            body = json.loads(resp.body)

            if (body["error_code"] > 0):
                raise SendMessageApiError()
            self.session["confirmCode"] = '%s' % code
            self.session.save();
            result = JsonTemplate.newJsonRes()
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())

class CheckPhoneHandle(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self,input):
        x = yield self.check_phone(input)
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def check_phone(self,phone):
        try:
            self.userService.getByPhone(phone)

            result = JsonTemplate.newJsonRes()

        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())
