#/usr/bin/python
#coding: utf-8

# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import tornado
from tornado.web import authenticated
from tornado import gen

from error.zebraError import *
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate
from utils.Constants import SessionUserID
from utils.jsonUtil import JsonBikeCtl
from dao.redisDao import RedisCache



# /wx/b/ctrl/cmd
class BikeCtrlHandler(BaseHandler):
    def get(self, cmd):
        try:
            user_id = self.session[SessionUserID]
            bikeID = self.get_argument("bikeID")
            self.bikeService.sendCtrlCmd(bikeID,user_id,cmd)
            result = JsonTemplate.newJsonRes().setErrMsg("OK").toJson()
        except Exception as e:
            print e
            result = JsonTemplate.newErrorJsonRes().setBody("error argument").toJson()
        self.write(result)
        pass

class NearBikeHandler(BaseHandler):
    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        result = yield self.get_result()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                lng = float(self.get_argument("lng"))
                lat = float(self.get_argument("lat"))
                distance = int(self.get_argument("distance"))

            except Exception as e:
                raise InputArgsError()

            bikeList = self.bikeService.getNearIdleBIke(lng, lat, distance)
            ret = JsonTemplate.newJsonRes().setBody(bikeList)
        except ZebraError as e:
            ret = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            ret = JsonTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())

class BikeInfoHandler(BaseHandler):
    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        result = yield self.get_result()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                bike_id = self.get_argument("bikeID")
            except Exception as e:
                raise InputArgsError()

            bike = self.bikeService.getBikeInfo(bike_id)
            if (bike == None):
                raise BikeNotFoundError()
            ret = JsonTemplate.newJsonRes().setBody(bike)
        except ZebraError as e:
            ret = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            ret = JsonTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())
