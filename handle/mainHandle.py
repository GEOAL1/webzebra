#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
from tornado.web import authenticated;

from handle.baseHandle import BaseHandler
from utils.Constants import SessionUserID
from utils.session import Session


class MainHandler(BaseHandler):
    @authenticated
    def get(self):
        user_id = self.session[SessionUserID]
        order = self.orderService.getUserOrderByUserID(user_id);
        if(order != None):
            self.redirect("/static/bikeInfo.html?order_id=%s" % (order["order_id"]))
        else:
            self.redirect("/static/panel.html");