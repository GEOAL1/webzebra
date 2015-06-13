#/usr/bin/python
#coding: utf-8
import time
import datetime
from error.zebraError import BalanceIsNoEngoughError, OrderOwnerError, BikeIsOnServiceError, GenOrderError
from service.IService import IService
import pytz


class OrderService(IService):
    def orderBike(self,user_id,bike_id):
        user = self.userDao.selecUserInfoByUid(user_id)
        bike = self.bikeDao.getBikeDyInfoByid(bike_id)
        if(bike.order_state == 1):
            raise BikeIsOnServiceError()
            raise
        if(user.balance < 10):
            raise BalanceIsNoEngoughError()


        result = self.orderDao.orderBike(user_id,bike_id,bike.mileage)
        if(result == None):
            raise GenOrderError

        pass

    def getUserOrderByUserID(self,user_id):
        return self.orderDao.getUserOrderByUserID(user_id)


    def getUserOrderByOrderID(self,order_id):
        return self.orderDao.getUserOrderByOrderID(order_id)

    def getPrice(self,costTime,mileage):
        timePrice = costTime / 60 * 1
        mileagePrice = 0.8 * (mileage / 1000.0) * 10

        if timePrice < mileagePrice:
            cost = mileagePrice
        else:
            cost = timePrice

        if(cost < 10):
            cost = 10
        return cost

    def finishOrder(self,order_id,user_id):
        user = self.userDao.selecUserInfoByUid(user_id)
        order = self.getUserOrderByOrderID(order_id)

        if(order.user_id != int(user_id)):
            raise OrderOwnerError()

        bike  = self.bikeDao.getBikeDyInfoByid(order.bike_id)

        startTime = int(time.mktime(order.order_time.timetuple())) +3600*8;

        finishTime = int(time.time())
        costTime =(finishTime - startTime)
        mileage = bike.mileage - order.begin_mileage
        if(mileage < 0 ):
            mileage=0

        price = self.getPrice(costTime,mileage)
        result = self.orderDao.finishOrder(order,costTime,mileage,price,startTime,finishTime)
        self.bikeDao.lockBike(order.bike_id)

        return price
        #lockBike
