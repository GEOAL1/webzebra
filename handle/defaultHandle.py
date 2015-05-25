#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import tornado
from handle.baseHandle import BaseHandler
from utils.AuthorUtils import login_required
from tornado.web import authenticated;

class DefaultHandler(BaseHandler):

    def get(self):
        None