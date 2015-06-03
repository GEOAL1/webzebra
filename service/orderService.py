#/usr/bin/python
#coding: utf-8
from service.IService import IService


class OrderService(IService):
    def orderBike(self,user_id,bike_id):
        return self.orderDao.orderBike(user_id,bike_id)
        pass

    def getUserOrderByUserID(self,user_id):
        return self.orderDao.getUserOrderByUserID(user_id)


    def getUserOrderByOrderID(self,order_id):
        return self.orderDao.getUserOrderByOrderID(order_id)

    def finishOrder(self,order_id):
        return self.orderDao.finishOrder(order_id)