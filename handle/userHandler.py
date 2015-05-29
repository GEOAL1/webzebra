# /usr/bin/python
# coding: utf-8
from tornado.web import authenticated

from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class userInfoHandler(BaseHandler):
    @authenticated
    def get(self):
        user = self.get_current_user()
        body = {'phone': user, 'totalScore': 1288, 'acctRemain': 159, 'totalKm': 159, 'totalTime': 5000,
                'remainKm': 128, 'remainTime': 1000}
        self.write(JsonTemplate.newJsonRes().setErrMsg("success").setBody(body).toJson())
