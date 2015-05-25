#/usr/bin/python
# coding: utf-8
from wsgiref.handlers import BaseHandler
import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from utils import session

from tornado.options import define, options
define("port", default=8001, help="run on the given port", type=int)



class MainHandler(BaseHandler):
    @login_required
    def get(self):
        username = self.get_current_user()
        print 'start..\n'
        print username
        print self.session['nima']
        if username==None:
            self.write('nima')
        else:
            self.write("What's up, " + username + "?")

class LoginHandler(BaseHandler):
    def get(self):
        self.session["user_name"] = self.get_argument("name")
        self.session["nima"] = 'xiaorui.cc'
        self.session.save()
        self.write(r'你的session已经欧了'.encode('utf-8'))


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret = "e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            session_secret = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout = 60,
            store_options = {
                'redis_host': '10.111.32.61',
                'redis_port': 6379,
                'redis_pass': '123456',
                },
        )
        handlers = [
            (r"/", MainHandler),
            (r"", MainHandler),
            (r"/login", LoginHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = session.SessionManager(settings["session_secret"], settings["store_options"], settings["session_timeout"])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
