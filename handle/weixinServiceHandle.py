# /usr/bin/python
# coding: utf-8
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class WeixinServiceHandle(BaseHandler):
    def get(self, cmd):
        if (cmd == "echo"):
            echostr = self.get_argument("echostr");
            self.write(echostr)
        pass

        if (cmd == "get_js_config"):
            try:
                refer = self.request.headers["Referer"]
                print refer
            except Exception as e:
                self.write(JsonTemplate.newErrorJsonRes().toJson())
                return
            result = JsonTemplate.newJsonRes().setBody(
                self.weixinManager.getJsJDK(self.request.headers["Referer"])).toJson()
            print result

            self.write(result)
        pass
    pass