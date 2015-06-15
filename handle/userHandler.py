# /usr/bin/python
# coding: utf-8
import base64
import json
import random
import tornado
from tornado.web import authenticated
from tornado import gen

from error.zebraError import *
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID, SessionPhone, SessionConfirmCode
from utils.messageUtils import MessageUtile


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




class FindPasswordHandle(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # 验证用户名和密码dd
        result = yield self.get_result()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            phone,password = self.checkArgs()
            self.userService.updatePasswordByPhone(phone,password)
            result = JsonTemplate.newJsonRes().setErrMsg("注册成功")
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())

    def checkArgs(self):
        try:
            phone = self.get_argument("ph")
            password = self.get_argument("pw")

            #confirmCode1 = self.get_argument("confirmCode")
            #confirmCode2 = self.session[SessionConfirmCode]
            phone = base64.decodestring(phone)
        except Exception as e:
            raise InputArgsError()
        '''
        if(confirmCode1 != confirmCode2):
            raise ValidateCodeError()
        '''
        return phone,password

