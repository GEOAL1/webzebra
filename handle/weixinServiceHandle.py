# /usr/bin/python
# coding: utf-8
import tornado
from tornado.web import authenticated
from tornado import gen

from error.zebraError import InputArgsError, ZebraError
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class WeixinServiceHandle(BaseHandler):
    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, cmd):
        x = yield self.get_result(cmd)
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self, cmd):
        if (cmd == "service"):
            echostr = self.get_argument("echostr");
            return gen.Return(echostr)
        pass

        if (cmd == "get_js_config"):
            try:
                refer = self.request.headers["Referer"]
            except Exception as e:
                raise InputArgsError()

            try:
                result = JsonTemplate.newJsonRes().setBody(
                    self.weixinManager.getJsJDK(self.request.headers["Referer"]))
            except ZebraError as e:
                result = JsonTemplate.newZebraErrorRes(e)
            except Exception as e:
                result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
            finally:
                raise gen.Return(result.toJson())
