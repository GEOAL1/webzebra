# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import tornado
from tornado.web import authenticated;

from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class RegHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        yield tornado.gen.Task(self.reg);
        self.finish();

    def reg(self):
        username = self.get_argument("un")
        password = self.get_arguments("pw")
        retryPassword = self.get_arguments("rpw")
        mcode1 = self.get_argument("mcode")
        mcode2 = self.session["mcode"]

        if not mcode2 and mcode1 == mcode2:
            if not password and password == retryPassword:
                if self.userService.getByUsername(username):
                    self.userService.add(username, password)
                else:
                    self.write(JsonTemplate.newErrorJsonRes().setErrMsg("用户名已存在或格式不正确"))
            else:
                self.write(JsonTemplate.newErrorJsonRes().setErrMsg("密码不相同或格式不正确"))

        else:
            self.write(JsonTemplate.newErrorJsonRes().setErrMsg("验证码不正确或没有验证码"))
