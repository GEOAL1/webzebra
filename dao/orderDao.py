#!/usr/bin/env python
#coding=utf-8
from dao.IMysqlDao import IMysqlDao


class OrderDao(IMysqlDao):
    def orderBike(self,user_id,bike_id):
        result = self.db.execute_rowcount("call order_bike(%s,%s)",bike_id,user_id);
        return result
    pass
