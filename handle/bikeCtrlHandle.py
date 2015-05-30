# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate

# /wx/b/ctrl/cmd
class BikeCtrlHandler(BaseHandler):
    def get(self, cmd):
        try:
            bikeID = self.get_argument("bikeID")
            if cmd == "voice":
                result = JsonTemplate.newJsonRes().setErrMsg(
                    "user : %s control bikeid %s voice" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "order":
                result = JsonTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s order" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "light":
                result = JsonTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s light" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "lock":
                result = JsonTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s lock" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "unlock":
                result = JsonTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s unlock" % (self.get_current_user(), bikeID)).toJson()
        except Exception as e:
            print e
            result = JsonTemplate.newErrorJsonRes().setBody("error argument").toJson()
        self.write(result)
        pass
