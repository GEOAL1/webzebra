# /usr/bin/python
# coding: utf-8
from datetime import datetime
import json
from tornado.web import authenticated

from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from tornado.escape import json_encode
from utils.Constants import SessionUserID


class UserInfoHandler(BaseHandler):
    @authenticated
    def get(self):
        user_id = self.session[SessionUserID]

        body = self.userService.selecDInfoByUserID(user_id)
        if(body == None) :
            self.write(JsonTemplate.setErrMsg(-1).setErrMsg("没有找到该用户").toJson())
            return
        body["password"] = ""
        print body
        self.write(JsonTemplate.newJsonRes().setErrMsg("success").setBody(body).toJson())
        print(JsonTemplate.newJsonRes().setErrMsg("success").setBody(body).toJson())



