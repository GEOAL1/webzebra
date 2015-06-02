#/usr/bin/python
#coding: utf-8
from service.IService import IService


class OrderService(IService):
    def orderBike(self,user_id,bike_id):
        return self.orderDao.orderBike(user_id,bike_id)
        pass