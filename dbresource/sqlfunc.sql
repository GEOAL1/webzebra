DELIMITER $$
use zebra$$
DROP PROCEDURE IF EXISTS order_bike;
create procedure order_bike(bikeid INT,userid int)
  begin
    DECLARE order_bike_id int;
    DECLARE order_user_id int;
    DECLARE txn_error INTEGER DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION BEGIN
      SET txn_error=1;
    END;

    START TRANSACTION;

    SELECT user_id into order_user_id from t_order where t_order.user_id = userid;

    SELECT bike_id into order_bike_id
    FROM b_bike_dynamic
    WHERE order_state=0 and bike_id=bikeid FOR UPDATE ;

    if(order_bike_id is not Null and order_user_id is Null) THEN
      update b_bike_dynamic set order_state=1 WHERE bike_id = order_bike_id;
      INSERT INTO t_order(bike_id, user_id)  VALUES(order_bike_id,userid);

      IF(txn_error) THEN
        ROLLBACK;
      ELSE
        SELECT LAST_INSERT_ID();
        COMMIT;
      END IF;
    ELSE
      ROLLBACK;
    END IF ;
  end$$

DROP PROCEDURE IF EXISTS cancel_order;
CREATE PROCEDURE cancel_order(orderid int)
  BEGIN

    DECLARE txn_error INTEGER DEFAULT 0;

    DECLARE  f_cost int;
    DECLARE  f_userid int;
    DECLARE  f_bikeid int;
    DECLARE  f_ordertime TIMESTAMP;
    DECLARE  f_mileage int;



    #计算本次消费金额
    DECLARE  order_cursor CURSOR FOR
      SELECT
      MINUTE(TIMEDIFF(NOW(),order_time)) as cost,
      user_id,bike_id,order_time,mileage
    from t_order WHERE order_id=orderid;

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION BEGIN
      SET txn_error=1;
    END;

    open order_cursor;
    FETCH order_cursor INTO f_cost,f_userid,f_bikeid,f_ordertime,f_mileage;
    close order_cursor;

    START TRANSACTION;
    #更新帐户
    UPDATE sys_user set balance=(balance - (f_cost+1)) WHERE  f_userid = user_id;

    #将本次消费记录 放入历史表
    INSERT INTO u_d_history(order_id,user_id, bike_id, mileage, costTime, start_time, end_time,cost)
      VALUES (orderid,f_userid,f_bikeid,f_mileage,f_cost,f_ordertime,now(),f_cost+1);

    #删除此订单信息
    DELETE  from t_order where orderid = order_id;

    #恢复车辆状态
    UPDATE b_bike_dynamic SET order_state = 0;

    if(txn_error) THEN
      ROLLBACK;
    ELSE
      SELECT 0 as state,"success" as message;
      COMMIT;
    END IF ;
  END$$

DROP FUNCTION IF EXISTS fun_distance;

CREATE FUNCTION fun_distance(lat1 float,lng1 float,lat2 float,lng2 float) RETURNS float
  BEGIN
    set @num=2 * 6378.137*ASIN(SQRT(POW(SIN(PI()*(lat1-(lat2))/360),2)+ COS(PI()*lat1/180)*COS(lat2*PI()/180)*POW(SIN(PI()*(lng1-(lng2))/360),2)));
    RETURN @num;
  END$$

DELIMITER ;


