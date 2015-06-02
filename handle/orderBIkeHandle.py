#/usr/bin/python
#coding: utf-8
from tornado.web import authenticated
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID


class OrderBikeHandler(BaseHandler):
    # @tornado.web.asynchronous
    # @tornado.gen.engine
    @authenticated
    def post(self):
        result = ""
        user_id = self.session[SessionUserID]
        try:
            bike_id = self.get_argument("bike_id")
            self.orderService.orderBike(user_id,bike_id)
            result = JsonTemplate.newJsonRes().toJson()
        except Exception as e :
            print e
            JsonTemplate.newErrorJsonRes().toJson()

        self.write(result)
        pass

