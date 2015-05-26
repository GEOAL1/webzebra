#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate, ErrorCode


class LoginHandler(BaseHandler):
    # @tornado.web.asynchronous
    # @tornado.gen.engine
    def get(self):
        self.render("login.html")

    def post(self):
        # 验证用户名和密码dd
        username = self.get_argument("un");
        password = self.get_argument("pw");
        if (self.userService.validateUP(username, password)):
            # do username and
            self.write(JsonTemplate.newJsonRes().setErrorCode(ErrorCode.success).toJson());
            self.session["un"] = username;
            self.session.save()
        else:
            self.write(JsonTemplate.newJsonRes().setErrorCode(ErrorCode.error).setErrMsg("用户名或密码不正确").toJson());
