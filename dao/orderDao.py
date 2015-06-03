#!/usr/bin/env python
#coding=utf-8
from dao.IMysqlDao import IMysqlDao


class OrderDao(IMysqlDao):
    def orderBike(self,user_id,bike_id):
        result = self.db.get("call order_bike(%s,%s)",bike_id,user_id);
        return result
    pass

    def finishOrder(self,order_id):
        result = self.db.execute_rowcount("call cancel_order(%s)",order_id);
        return result

    def getUserOrderByUserID(self,user_id):
        sql = "select * from t_order where user_id = %s";
        return self.db.get(sql,user_id)

    def getUserOrderByOrderID(self,order_id):
        sql = "select *,MINUTE(TIMEDIFF(NOW(),order_time)) as cost_time  from t_order where order_id = %s";
        return self.db.get(sql,order_id)