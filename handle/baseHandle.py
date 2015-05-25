#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import tornado
from utils import session


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = session.Session(self.application.session_manager, self)
    def get_current_user(self):
        print(self.session.get("user_name"))
        return self.session.get("user_name")

