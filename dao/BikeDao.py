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
    defaultSelectSql = "select * from b_bike_common,b_bike_dynamic where %s"
    
    def selectDyAll(self):
        return self.db.query(self.defaultDynamicSelectSql % "1");
    
    
    def getRangeeDyByLoLa(self,centerLo,centerLa,scopeRange):
        cond = "sqrt((((%f-longitude)*PI()*12656*cos(((%f+latitude)/2)*PI()/180)/180)*((%f-longitude)*PI()*12656*cos (((%f+latitude)/2)*PI()/180)/180))+(((%f-latitude)*PI()*12656/180)*((%f-latitude)*PI()*12656/180)))<%f" % (centerLo, centerLa, centerLo, centerLa, centerLa, centerLa,scopeRange);
        sql = self.defaultDynamicSelectSql % (cond)
        ret = self.db.query(sql);
        return ret
    
    def setBikeeDyInfoById(self,bikeDynamicInfo):                                                              
        sql = "update b_bike_dynamic set cur_power = %d ,throttle_state = '%s',brake_state = '%s',motor_state = '%s',lock_state = '%s',indicator_state = '%s',longitude = %f,latitude = %f,speed = %f,mileage = %f , time_samp = '%s' where bike_id = %d" % (bikeDynamicInfo["cur_power"],bikeDynamicInfo["throttle_state"],bikeDynamicInfo["brake_state"],bikeDynamicInfo["motor_state"],bikeDynamicInfo["lock_state"],bikeDynamicInfo["indicator_state"],bikeDynamicInfo["longitude"],bikeDynamicInfo["latitude"],bikeDynamicInfo["speed"],bikeDynamicInfo["mileage"],bikeDynamicInfo["timesamp"],bikeDynamicInfo["bike_id"])   
        print(sql)
        self.db.execute(sql)
    
    def getBikeDyInfoByid(self,bikeId):
        cond = "bike_id = %d" % bikeId
        sql = self.defaultDynamicSelectSql % (cond)
        ret = self.db.query(sql)
        return ret
        
    def selectCommonAll(self):
        return self.db.query(self.defaultCommonSelectSql % "1");
    
    def getBikeCommonInfoByid(self,bikeId):
        cond = "bike_id = %d" % bikeId
        sql = self.defaultCommonSelectSql % (cond)
        ret = self.db.query(sql)
        return ret
    
    def getRangeByLoLa(self,centerLo,centerLa,scopeRange):
        cond = "sqrt((((%f-longitude)*PI()*12656*cos(((%f+latitude)/2)*PI()/180)/180)*((%f-longitude)*PI()*12656*cos (((%f+latitude)/2)*PI()/180)/180))+(((%f-latitude)*PI()*12656/180)*((%f-latitude)*PI()*12656/180)))<%f" % (centerLo, centerLa, centerLo, centerLa, centerLa, centerLa,scopeRange);
        sql = self.defaultSelectSql % (cond)
        ret = self.db.query(sql);
        return ret
    
    def getBikeInfoByid(self,bikeId):
        cond = "b_bike_common.bike_id = %d" % bikeId
        sql = self.defaultSelectSql % (cond)
        ret = self.db.query(sql)
        return ret
    
if __name__ == '__main__':

    dao = BikeDao();
    FORMAT_TIME = "%Y-%m-%d %H:%M:%S"
    info = BikeDynamicInfo()
    info.bike_id = 10000001
    info.cur_power = 50
    info.throttle_state = "on"
    info.brake_state = "on"
    info.motor_state = "on"
    info.lock_state = "on"
    info.indicator_state = "on"
    info.longitude = 145.3333
    info.latitude = 35.333
    info.speed = 0
    info.mileage = 0
    info.timesamp =  time.strftime( FORMAT_TIME, time.localtime() )
    dao.setBikeInfoById(info.__dict__)
    print dao.selectAll()
    print dao.getRangeeDyByLoLa(116.440255, 39.947385, 0.5)
    print dao.getRangeByLoLa(116.440255, 39.947385, 0.5)
    print dao.getBikeInfoByid(10000001)
    print dao.getBikeDyInfoByid(10000001)
    print dao.getBikeCommonInfoByid(10000001)
    
