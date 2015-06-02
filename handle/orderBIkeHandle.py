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
    def get(self):
        result = ""
        user_id = self.session[SessionUserID]
        try:
            bike_id = self.get_argument("bikeID")
            if(self.orderService.orderBike(user_id,bike_id) > 0):
                result = JsonTemplate.newJsonRes().toJson()
            else:
                result = JsonTemplate.newErrorJsonRes().toJson()
        except Exception as e :
            print e
            JsonTemplate.newErrorJsonRes().toJson()

        self.write(result)
        pass

