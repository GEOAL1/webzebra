#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
from tornado.web import authenticated;

from handle.baseHandle import BaseHandler


class MainHandler(BaseHandler):
    @authenticated
    def get(self):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1

        countString = "1 time" if count == 1 else "%d times" % count

        self.set_secure_cookie("count", str(count))

        self.write(
            '<html><head><title>Cookie Counter</title></head>'
            '<body><h1>You ve viewed this page %s times.</h1>' % countString +
            '</body></html>'
        )