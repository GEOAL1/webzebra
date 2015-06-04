#/usr/bin/python
#coding: utf-8
import tornado
from tornado.web import authenticated
from error.zebraError import *
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID
from tornado import gen

class OrderBikeHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @authenticated
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                user_id = self.session[SessionUserID]
                bike_id = self.get_argument("bikeID")
            except Exception as e:
                raise InputArgsError()

            order_id = self.orderService.orderBike(user_id,bike_id)
            if order_id is None:
                raise GenOrderError()
            result = JsonTemplate.newJsonRes().setBody(order_id)

        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())

class GetOrderHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @authenticated
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()
    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                order_id=self.get_argument("order_id")
            except Exception as e:
                raise InputArgsError()

            order = self.orderService.getUserOrderByOrderID(order_id)

            if order is None:
                raise OrderNotFoundError()
            if order["user_id"] != long(self.session[SessionUserID]):
                raise OrderOwnerError()
            result = JsonTemplate.newJsonRes().setBody(order)
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())
        pass

class FinishOrderHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @authenticated
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                order_id=self.get_argument("order_id")
            except Exception as e:
                raise InputArgsError()

            if self.orderService.finishOrder(order_id) <= 0:
                raise FinishOrderError()

            result = JsonTemplate.newJsonRes().setErrMsg("取消订单成功")
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())
        pass

class GetOrderByUserIDHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    @authenticated
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                user_id=self.get_argument("user_id")
            except Exception as e:
                raise InputArgsError()

            order = self.orderService.getUserOrderByUserID(user_id)

            if(order is None):
                raise UserOrderNotFoundError()
            body = {"order_id":order["order_id"]}
            result = JsonTemplate.newJsonRes().setBody(body)

        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())
        pass



