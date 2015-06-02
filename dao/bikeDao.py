# /usr/bin/python
# coding: utf-8
from dao.IMysqlDao import IMysqlDao
from model.BikeDynamic import BikeDynamicInfo
import time


class BikeDao(IMysqlDao):
    
    def __init__(self):
        pass
    
    defaultDynamicSelectSql = "select * from b_bike_dynamic where %s"
    defaultCommonSelectSql = "select * from b_bike_common where %s"

    '''
        动态表操作
    '''
    def selectDyAll(self):
        return self.db.query("select * from b_bike_dynamic");

    def getRangeeDyByLoLa(self,centerLo,centerLa,scopeRange):
        sql = "select b_bike_dynamic.*, fun_distance(%s,%s,latitude,longitude) as distance from b_bike_dynamic  where fun_distance(%s,%s,latitude,longitude) < %s"
        ret = self.db.query(sql, centerLa, centerLo,centerLa, centerLo,scopeRange/1000.0);
        return ret
    
    def setBikeeDyInfoById(self,bikeDynamicInfo):                                                              
        sql = "update b_bike_dynamic set cur_power = %d ,throttle_state = '%s',brake_state = '%s',motor_state = '%s',lock_state = '%s',indicator_state = '%s',longitude = %f,latitude = %f,speed = %f , time_samp = '%s' where bike_id = %d" % (bikeDynamicInfo["cur_power"],bikeDynamicInfo["throttle_state"],bikeDynamicInfo["brake_state"],bikeDynamicInfo["motor_state"],bikeDynamicInfo["lock_state"],bikeDynamicInfo["indicator_state"],bikeDynamicInfo["longitude"],bikeDynamicInfo["latitude"],bikeDynamicInfo["speed"],bikeDynamicInfo["timesamp"],bikeDynamicInfo["bike_id"])
        print(sql)
        self.db.execute(sql)
    
    def getBikeDyInfoByid(self,bikeId):
        cond = "bike_id = %d" % bikeId
        sql = self.defaultDynamicSelectSql % (cond)
        ret = self.db.query(sql)
        return ret


    """
        静态表操作
    """


    
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

    print dao.getRangeeDyByLoLa(116.440255, 39.947385,10000.0)