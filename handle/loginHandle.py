#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import tornado
from tornado import  gen

from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate, ErrorCode
from utils.Constants import SessionUsername


class LoginHandler(BaseHandler):
    # @tornado.web.asynchronous
    # @tornado.gen.engine
    def get(self):
        self.redirect("/static/login.html")

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        # 验证用户名和密码dd
        result = yield self.validateUser()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def validateUser(self):
        try:
            username = self.get_argument("un")
            password = self.get_argument("pw")
            if (self.userService.getByUP(username, password)):
                self.session[SessionUsername] = username;
                self.session.save()
                ret = JsonTemplate.newJsonRes().setErrorCode(ErrorCode.success).toJson()
            else:
                ret = JsonTemplate.newJsonRes().setErrorCode(ErrorCode.error).setErrMsg("用户名或密码不正确").toJson()
        except Exception as e:
            ret = JsonTemplate.newErrorJsonRes().setErrMsg("unknow error").toJson();
        raise gen.Return(ret)