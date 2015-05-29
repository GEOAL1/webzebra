#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import tornado
from tornado.web import RequestHandler

from service.userService import UserService
from utils import session
from utils.Constants import SessionUsername
from utils.WeixinUtils import WeixinMananger


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = session.Session(self.application.session_manager, self)
        self.userService = UserService();
        # self.userService = self.application.userService
        self.weixinManager = WeixinMananger()
        # self.weixinManager = self.application.weixinManager

    def get_current_user(self):
        return self.session.get(SessionUsername)
