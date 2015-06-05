# /usr/bin/python
# coding: utf-8
import os;

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

from handle.amountHandle import RechargeHandler
from handle.bikeHandle import NearBikeHandler, BikeCtrlHandler, BikeInfoHandler
from handle.defaultHandle import DefaultHandler
from handle.loginHandle import LoginHandler
from handle.mainHandle import MainHandler
from handle.orderHandle import GetOrderHandler, OrderBikeHandler, FinishOrderHandler, GetOrderByUserIDHandler
from handle.regHandle import RegHandler, SendPhoneCodeHandle, CheckPhoneHandle
from handle.userHandler import UserInfoHandler
from handle.weixinServiceHandle import WeixinServiceHandle
from service.amountService import AmountService
from service.bikeService import BikeService
from service.orderService import OrderService
from service.userService import UserService
from utils import session
from utils.WeixinUtils import WeixinMananger

define("port", default=8001, help="run on the given port", type=int)


class ZebraApplicatoin(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            session_secret="3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout=600,

            store_options={
                'redis_host': 'localhost',
                'redis_port': 6379,
                'redis_pass': '',
            },

            debug=True,
            login_url="/wx/u/login",
            template_path=os.path.join(os.path.dirname(__file__), "t"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),

        )
        handlers = [
            (r"/", MainHandler),
            (r"", MainHandler),
            (r"/wx/u/login", LoginHandler),

            # 车辆管理OrderBikeHandler
            (r"/wx/b/list", DefaultHandler),
            (r"/wx/b/info", BikeInfoHandler),
            (r"/wx/b/ctrl/(\w*)", BikeCtrlHandler),
            (r"/wx/b/search", NearBikeHandler),

            #订单管理
            (r"/wx/o/order", OrderBikeHandler),
            (r"/wx/o/get"  , GetOrderHandler),
            (r"/wx/o/finish", FinishOrderHandler),


            # 用户信息管理
            (r"/wx/u/reg", RegHandler),
            (r"/wx/u/checkPhone/(\d{11})", CheckPhoneHandle),
            (r"/wx/u/info", UserInfoHandler),
            (r"/wx/u/order", GetOrderByUserIDHandler),

            #帐户管理
            (r"/wx/a/recharge", RechargeHandler),

            # 第三方服务
            (r"/wx/send/phoneCode", SendPhoneCodeHandle),

            # 微信服务
            (r"/wx/service/(.*)", WeixinServiceHandle)

        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = session.SessionManager(settings["session_secret"], settings["store_options"],
                                                      settings["session_timeout"])
        self.userService = UserService()
        self.bikeService = BikeService();
        self.weixinManager = WeixinMananger()
        self.amountService = AmountService()
        self.orderService = OrderService()

        # xsrf_cookies=True,


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = ZebraApplicatoin()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
