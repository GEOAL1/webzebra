#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
from tornado.web import authenticated;

from handle.baseHandle import BaseHandler


class MainHandler(BaseHandler):
    @authenticated
    def get(self):
        self.redirect("/static/panel.html");
