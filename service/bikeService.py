#/usr/bin/python
#coding: utf-8
from service.IService import IService


class BikeService(IService):

    def  getNearBIke(self,lng,lat,distance):
        return self.bikeDao.getRangeeDyByLoLa(lng,lat,distance)

    def getNearIdleBIke(self,lng,lat,distance):
        return self.bikeDao.getIdleRangeeDyByLoLa(lng,lat,distance)

    def getBikeDetailInfo(self,bike_id):
        return self.bikeDao.getBikeDyInfoByid(bike_id)
		
	def selectCommonAll(self):
        return self.bikeDao.selectCommonAll()
    
    def selectCommonTimeAll(self,time):
        return self.bikeDao.selectCommonTimeAll(time)