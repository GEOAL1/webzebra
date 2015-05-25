#/usr/bin/python
# coding: utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
from handle.loginHandle import LoginHandler
from handle.mainHandle import MainHandler
from utils import session

define("port", default=8000, help="run on the given port", type=int)
class ZebraApplicatoin(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret = "e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            session_secret = "3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout = 600,
            store_options = {
                'redis_host': '10.111.32.61',
                'redis_port': 6379,
                'redis_pass': '123456',
                },
            debug = True
        )
        handlers = [
            (r"/", MainHandler),
            (r"", MainHandler),
            (r"/login", LoginHandler)
            (r"/wx/login", LoginHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = session.SessionManager(settings["session_secret"], settings["store_options"], settings["session_timeout"])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = ZebraApplicatoin()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
