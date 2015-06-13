#!/usr/bin/env python
#coding=utf-8
from dao.IMysqlDao import IMysqlDao


class OrderDao(IMysqlDao):
    def orderBike(self,user_id,bike_id,mileage):
        result = self.db.get("call order_bike(%s,%s,%s)",bike_id,user_id,mileage);
        return result
    pass

    def finishOrder(self,order,costTime,mileage,price,startTime,finishTime):
        sql = "START TRANSACTION;" \
              "insert into t_order_history(user_id, bike_id, mileage, costTime, start_time, end_time, order_id, cost) " \
              "VALUE (%s,%s,%s,%s,from_unixtime(%s),from_unixtime(%s),%s,%s);" \
              "DELETE FROM t_order WHERE order_id = %s;" \
              "UPDATE t_bike_dynamic set order_state=0 where bike_id = %s;" \
              "UPDATE t_user " \
              "set balance = balance - %s , total_time = %s+total_time," \
              "points = %s," \
              "total_mileage=%s+total_mileage where user_id = %s;" \
              "COMMIT"
        result = self.db.execute(sql,order.user_id,order.bike_id,mileage,costTime,startTime,finishTime,
                                 order.order_id,price,
                                 order.order_id,
                                 order.bike_id,
                                 price,costTime,
                                 price,


                                 mileage,order.user_id)

        return result

    def getUserOrderByUserID(self,user_id):
        sql = "select *,TIMESTAMPDIFF(MINUTE,order_time,NOW()) as cost_time from t_order where user_id = %s";
        return self.db.get(sql,user_id)

    def getUserOrderByOrderID(self,order_id):
        sql = "select *,TIMESTAMPDIFF(MINUTE,order_time,NOW()) as cost_time  from t_order where order_id = %s";
        return self.db.get(sql,order_id)