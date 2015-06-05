#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import time

import tornado
from tornado.web import RequestHandler

from utils import session
from utils.Constants import SessionUserID


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = session.Session(self.application.session_manager, self)
        if (int(time.time()) - self.session["create_time"] > 30):
            self.session.save()

        """
        self.userService = UserService();
        self.bikeService = BikeService();
        self.weixinManager = WeixinMananger()
        self.amountService = AmountService()
        self.orderService = OrderService()
        """
        self.userService = self.application.userService
        self.bikeService = self.application.bikeService
        self.weixinManager = self.application.weixinManager
        self.amountService = self.application.amountService
        self.orderService = self.application.orderService

    def get_current_user(self):
        return self.session.get(SessionUserID)

    def get_result(self):
        pass
