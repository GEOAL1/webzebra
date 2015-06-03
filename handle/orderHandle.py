#/usr/bin/python
#coding: utf-8
from tornado.web import authenticated
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID, CookieLastOrderID, CookieLastCtrlBIke


class OrderBikeHandler(BaseHandler):
    # @tornado.web.asynchronous
    # @tornado.gen.engine
    @authenticated
    def get(self):
        result = ""
        user_id = self.session[SessionUserID]
        try:
            bike_id = self.get_argument("bikeID")
            print(bike_id)
            order_id = self.orderService.orderBike(user_id,bike_id)
            if(order_id != None):
                result = JsonTemplate.newJsonRes().toJson()
            else:
                result = JsonTemplate.newErrorJsonRes().toJson()
        except Exception as e :
            print e
            self.redirect("/")
            JsonTemplate.newErrorJsonRes().setErrMsg("请刷新后重试").toJson()
            return
        self.write(result)
        pass

class GetOrderHandler(BaseHandler):
    @authenticated
    def get(self):
        try:
            order_id=self.get_argument("order_id")
            order = self.orderService.getUserOrderByOrderID(order_id)
            if(order == None) :
                result = JsonTemplate.newErrorJsonRes().setErrMsg("没有找到该订单").setErrorCode(-1)
            else:
                if order["user_id"] != long(self.session[SessionUserID]):
                    result = JsonTemplate.newErrorJsonRes().setErrMsg("该订单不是该用户的").setErrorCode(-1)
                else:
                    result = JsonTemplate.newJsonRes().setBody(order)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg("无效的SQL语句或错误的参数").setErrorCode(-1)
        self.write(result.toJson())
        pass
class FinishOrderHandler(BaseHandler):
    @authenticated
    def get(self):
        try:
            order_id=self.get_argument("order_id");
            if(self.orderService.finishOrder(order_id)<=0):
                result = JsonTemplate.newErrorJsonRes().setErrMsg("取消订单失败")
            else:
                result = JsonTemplate.newJsonRes().setErrMsg("取消订单成功")
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg("取消订单失败")

        self.write(result.toJson())



