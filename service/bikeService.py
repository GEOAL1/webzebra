#/usr/bin/python
#coding: utf-8
from dao.redisDao import RedisCache
from error.zebraError import InvaildBikeCtrlCmdError
from service.IService import IService
from utils.jsonUtil import JsonBikeCtl



class BikeService(IService):

    def  getNearBIke(self,lng,lat,distance):
        return self.bikeDao.getRangeeDyByLoLa(lng,lat,distance)

    def getNearIdleBIke(self,lng,lat,distance):
        return self.bikeDao.getIdleRangeeDyByLoLa(lng,lat,distance)

    def getBikeDetailInfo(self, lng, lat, bike_id):
        return self.bikeDao.getBikeDetailInfoByID(lng, lat, bike_id)

    def getBikeInfo(self, bike_id):
        return self.bikeDao.getBikeDyInfoByid(bike_id)
    def selectCommonAll(self):
        return self.bikeDao.selectCommonAll()
    def selectCommonTimeAll(self,time):
        return self.bikeDao.selectCommonTimeAll(time)
    
    def setBikeeDyInfoById(self,bikeDynamicInfo): 
        self.bikeDao.setBikeeDyInfoById(bikeDynamicInfo)  
           
    def setCurPower(self,cur_power,bikeID):
        self.bikeDao.setCurPower(cur_power,bikeID)
        
    def setThrottleState(self,throttle_state,bikeID):
        self.bikeDao.setThrottleState(throttle_state,bikeID)
        
    def setBrakeState(self,brake_state,bikeID):
        self.bikeDao.setBrakeState(brake_state,bikeID)
        
    def setMotorState(self,motor_state,bikeID):
        self.bikeDao.setMotorState(motor_state,bikeID)
        
    def setLockState(self,lock_state,bikeID):
        self.bikeDao.setLockState(lock_state,bikeID)
        
    def setIndicatorState(self,indicator_state,bikeID):
        self.bikeDao.setIndicatorState(indicator_state,bikeID)
        
    def setLoLa(self,longitude,latitude,bikeID):
        self.bikeDao.setLoLa(longitude,latitude,bikeID)
    
    def setSpeed(self,speed,bikeID):
        self.bikeDao.setSpeed(speed,bikeID)

    def sendCtrlCmd(self,bikeID,user_id,cmd):
        ctrl = JsonBikeCtl()
        ctrl.setBikeID(bikeID)

        if cmd == "voice":
            ctrl.setHorn(1)
        elif cmd == "light":
            ctrl.setIndicatorLight(1)
        elif cmd == "lock":
            ctrl.setLockBike(1)
        elif cmd == "unlock":
            ctrl.setLockBike(0)
        else:
            raise InvaildBikeCtrlCmdError()

        ctrlRet = ctrl.tojsonStr()

        RedisCache().listRpush("bikeCtrlTopic", ctrlRet)


