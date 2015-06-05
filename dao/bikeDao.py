# /usr/bin/python
# coding: utf-8
import time

from dao.IMysqlDao import IMysqlDao
from model.BikeDynamic import BikeDynamicInfo


class BikeDao(IMysqlDao):
    
    def __init__(self):
        pass
    
    defaultDynamicSelectSql = "select * from b_bike_dynamic where %s"
    defaultCommonSelectSql = "select * from b_bike_common where %s"

    '''
        动态表操作
    '''
    def selectDyAll(self):
        return self.db.query(self.defaultDynamicSelectSql % "1");

    def getRangeeDyByLoLa(self,centerLo,centerLa,scopeRange):
        sql = "select a.*,b.price, fun_distance(%s,%s,latitude,longitude) as distance from b_bike_dynamic a  join  b_bike_common b  on " \
              " a.bike_id = b.bike_id  and fun_distance(%s,%s,a.latitude,a.longitude) < %s "
        ret = self.db.query(sql, centerLa, centerLo,centerLa, centerLo,scopeRange/1000.0);
        return ret

    def getIdleRangeeDyByLoLa(self,centerLo,centerLa,scopeRange):
        sql = "select a.*,b.price, fun_distance(%s,%s,latitude,longitude) as distance from b_bike_dynamic a  join  b_bike_common b  on " \
              " a.bike_id = b.bike_id and a.order_state = 0 and fun_distance(%s,%s,a.latitude,a.longitude) < %s "
        ret = self.db.query(sql, centerLa, centerLo,centerLa, centerLo,scopeRange/1000.0);
        return ret


    def getBikeDetailInfoByID(self, centerLo, centerLa, bike_id):
        sql = "select a.*,b.price, fun_distance(%s,%s,latitude,longitude) as distance from b_bike_dynamic a  join  b_bike_common b  on  a.bike_id=%s and b.bike_id=%s"
        ret = self.db.query(sql, centerLa, centerLo, bike_id, bike_id);
        return ret

    def setBikeeDyInfoById(self,bikeDynamicInfo):                                                              
        sql = "update b_bike_dynamic set cur_power = %d ,throttle_state = '%s',brake_state = '%s',motor_state = '%s',lock_state = '%s',indicator_state = '%s',longitude = %f,latitude = %f,speed = %f , time_samp = '%s' where bike_id = %d" % (bikeDynamicInfo["cur_power"],bikeDynamicInfo["throttle_state"],bikeDynamicInfo["brake_state"],bikeDynamicInfo["motor_state"],bikeDynamicInfo["lock_state"],bikeDynamicInfo["indicator_state"],bikeDynamicInfo["longitude"],bikeDynamicInfo["latitude"],bikeDynamicInfo["speed"],bikeDynamicInfo["timesamp"],bikeDynamicInfo["bike_id"])
        print(sql)
        self.db.execute(sql)

    def getBikeDyInfoByid(self,bikeId):
        cond = "bike_id = %s"
        sql = self.defaultDynamicSelectSql % (cond)
        ret = self.db.get(sql,bikeId)
        return ret


    """
        静态表操作
    """
    def selectCommonAll(self):
        return self.db.query(self.defaultCommonSelectSql % "1");
    
    def getBikeCommonInfoByid(self,bikeId):
        cond = "bike_id = %d" % bikeId
        sql = self.defaultCommonSelectSql % (cond)
        ret = self.db.query(sql)
        return ret
    
    def selectCommonTimeAll(self,timeStr):
        crutime = time.mktime(time.strptime(timeStr,'%Y-%m-%d %H:%M:%S'))
        cond = "register_time > %s"
        sql = self.defaultCommonSelectSql % (cond)
        return self.db.query(sql,crutime)
    
if __name__ == '__main__':
    dao = BikeDao();
    FORMAT_TIME = "%Y-%m-%d %H:%M:%S"
    info = BikeDynamicInfo()
    info.bike_id = 10000001
    info.cur_power = 50
    info.throttle_state = "1"
    info.brake_state = "1"
    info.motor_state = "1"
    info.lock_state = "1"
    info.indicator_state = "1"
    info.longitude = 145.3333
    info.latitude = 35.333
    info.speed = 0
    info.timesamp =  time.strftime( FORMAT_TIME, time.localtime() )

    print dao.getRangeeDyByLoLa(116.440255, 39.947385,5000.0)