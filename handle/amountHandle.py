#/usr/bin/python
#coding: utf-8
from tornado.web import authenticated
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID


class RechargeHandler(BaseHandler):
    @authenticated
    def post(self):
        result = ""
        try:
            rechargeNum = float(self.get_argument("rechargeNum"))
            user_id = self.session[SessionUserID]
            if self.amountService.recharge(user_id,rechargeNum) > 0:
                result = JsonTemplate.newJsonRes().setErrMsg("success").toJson()
        except Exception as e :
            print e
            result = JsonTemplate.newErrorJsonRes().setErrMsg("充值失败").toJson()
            pass
        self.write(result)
        pass
