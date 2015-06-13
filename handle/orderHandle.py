#/usr/bin/python
#coding: utf-8
import tornado
from tornado.web import authenticated
from tornado import gen

from error.zebraError import *
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID


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

            self.orderService.orderBike(user_id,bike_id)

            result = JsonTemplate.newJsonRes().setBody("下单成功")

        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg("您已经订车，或刷新后再试")
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
                order_id = self.get_argument("order_id")
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
                order_id = self.get_argument("order_id")
                user_id = self.session[SessionUserID]
            except Exception as e:
                raise InputArgsError()

            price = self.orderService.finishOrder(order_id,user_id)
            result = JsonTemplate.newJsonRes().setErrMsg("订单成功，消费金额 %d 币" % (price) )
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            print e
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
            user_id = self.session[SessionUserID]

            order = self.orderService.getUserOrderByUserID(user_id)

            if (order is None):
                raise UserOrderNotFoundError()
            body = {"order_id": order["order_id"]}
            result = JsonTemplate.newJsonRes().setBody(body)

        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())
        pass
