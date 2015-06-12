# /usr/bin/python
# coding: utf-8
import tornado
from tornado.web import authenticated
from tornado import gen

from error.zebraError import *
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID


class UserInfoHandler(BaseHandler):

    @authenticated
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
            user_id = self.session[SessionUserID]
            body = self.userService.selecUserInfoByUid(user_id)
            if (body == None):
                raise UserIsNotFoundedError()
            body["password"] = ""
            result = JsonTemplate.newJsonRes().setBody(body)
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())
