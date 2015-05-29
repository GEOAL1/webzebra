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
        # 判断是否为微信用户，如果是，则存SESSION，和COOKIE后，直接重定向到主页，否则重定向到LOGIN页
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
                self.set_secure_cookie(SessionUsername, username)
                ret = JsonTemplate.newJsonRes().setErrorCode(ErrorCode.success).toJson()
            else:
                ret = JsonTemplate.newJsonRes().setErrorCode(ErrorCode.error).setErrMsg("用户名或密码不正确").toJson()
        except Exception as e:
            ret = JsonTemplate.newErrorJsonRes().setErrMsg("unknow error").toJson();
        raise gen.Return(ret)