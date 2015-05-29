# /usr/bin/python
# coding: utf-8
from handle.baseHandle import BaseHandler


class WeixinServiceHandle(BaseHandler):
    def get(self, cmd):
        if (cmd == "echo"):
            echostr = self.get_argument("echostr");
            self.write(echostr)
        pass

    pass
