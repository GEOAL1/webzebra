# /usr/bin/python
# coding: utf-8
import time

from dao.IMysqlDao import IMysqlDao
from model.BikeDynamic import BikeDynamicInfo


class BikeDao(IMysqlDao):
    
    FORMAT_TIME = "%Y-%m-%d %H:%M:%S"
    def __init__(self):
        pass
    
    defaultDynamicSelectSql = "select * from b_bike_dynamic where %s"
    defaultCommonSelectSql = "select * from b_bike_common where %s"
    defautlDyUpdateSql = "update b_bike_dynamic set"
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
        sql = "update b_bike_dynamic set cur_power = %d ,throttle_state = %d,brake_state = %d,motor_state = %d,lock_state = %d,indicator_state = %d,longitude = %f,latitude = %f,speed = %f , time_samp = '%s' where bike_id = %d" % (bikeDynamicInfo["cur_power"],bikeDynamicInfo["throttle_state"],bikeDynamicInfo["brake_state"],bikeDynamicInfo["motor_state"],bikeDynamicInfo["lock_state"],bikeDynamicInfo["indicator_state"],bikeDynamicInfo["longitude"],bikeDynamicInfo["latitude"],bikeDynamicInfo["speed"],bikeDynamicInfo["timesamp"],bikeDynamicInfo["bike_id"])
        self.db.execute(sql)

    def getBikeDyInfoByid(self,bikeId):
        cond = "bike_id = %s "
        sql = self.defaultDynamicSelectSql % (cond)
        ret = self.db.get(sql,bikeId)
        return ret
    
    def setCurPower(self,cur_power,bikeID):
        cond = "cur_power = %d , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,cur_power,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setThrottleState(self,throttle_state,bikeID):
        cond = "throttle_state = %d , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,throttle_state,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setBrakeState(self,brake_state,bikeID):
        cond = "brake_state = %d , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,brake_state,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setMotorState(self,motor_state,bikeID):
        cond = "motor_state = %d , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,motor_state,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setLockState(self,lock_state,bikeID):
        cond = "lock_state = %d , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,lock_state,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setIndicatorState(self,indicator_state,bikeID):
        cond = "indicator_state = %d , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,indicator_state,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setLoLa(self,longitude,latitude,bikeID):
        cond = "longitude = %f,latitude = %f , time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,longitude,latitude,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
        return ret
    def setSpeed(self,speed,bikeID):
        cond = "speed = %f, time_samp = '%s' "
        condw = "where  bike_id = %d"
        temp = self.defautlDyUpdateSql % (cond)
        sql = temp % (condw)
        ret = self.db.execute(sql,speed,time.strftime( FORMAT_TIME, time.localtime()),bikeID)
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
    print(dao.selectCommonTimeAll("2015-06-04 16:00:00"))
#     FORMAT_TIME = "%Y-%m-%d %H:%M:%S"
#     info = BikeDynamicInfo()
#     info.bike_id = 10000001
#     info.cur_power = 50
#     info.throttle_state = "1"
#     info.brake_state = "1"
#     info.motor_state = "1"
#     info.lock_state = "1"
#     info.indicator_state = "1"
#     info.longitude = 145.3333
#     info.latitude = 35.333
#     info.speed = 0
#     info.timesamp =  time.strftime( FORMAT_TIME, time.localtime())
# 
#     print dao.getRangeeDyByLoLa(116.440255, 39.947385,5000.0)