#/usr/bin/python
#coding: utf-8
from service.IService import IService


class BikeService(IService):

    def  getNearBIke(self,lng,lat,distance):
        return self.bikeDao.getRangeeDyByLoLa(lng,lat,distance)
