#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import base64
import tornado
from tornado import  gen
from tornado.web import authenticated

from error.zebraError import ZebraError, InputArgsError, UnameOrPasswordError
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID, SessionPhone


class LoginHandler(BaseHandler):

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
        ret = ""
        try:
            try:
                phone = self.get_argument("un");
                password = self.get_argument("pw");
                phone = base64.decodestring(phone)
            except Exception as e:
                raise InputArgsError();

            user = self.userService.getByPP(phone, password)

            if (user  != None):
                self.session[SessionUserID] = user["user_id"];
                self.session[SessionPhone] = phone
                self.session.save()
                ret = JsonTemplate.newJsonRes()
            else:
                raise UnameOrPasswordError();
        except ZebraError as e:
            ret = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            ret = JsonTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())
