#/usr/bin/python
#coding: utf-8
import tornado
from tornado.web import authenticated
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID
from tornado import gen
from error.zebraError import *

class RechargeHandler(BaseHandler):

    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        result = yield self.validateUser()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                rechargeNum = float(self.get_argument("rechargeNum"))
            except Exception as e:
                raise InputArgsError()

            user_id = self.session[SessionUserID]
            if self.amountService.recharge(user_id,rechargeNum) > 0:
                ret = JsonTemplate.newJsonRes();
        except ZebraError as e:
            ret = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            ret = JsonTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())
