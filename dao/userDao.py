# /usr/bin/python
# coding: utf-8
from dao.IMysqlDao import IMysqlDao
from error.zebraError import *
from model.User import User


class UserDao(IMysqlDao):
    def __init__(self):
        pass

    defaultSelectSql = "select * from sys_user where %s"

    def selectAll(self):
        return self.db.query(self.defaultSelectSql % "1");

    def add(self, user):
        sql = "insert into sys_user(phone_num,password) values(%s,%s)";
        xid = self.db.execute(sql, user["phone"], user["password"]);
        user["id"] = xid;
        if xid > 0:
            return user;
        else:
            raise CreateUserError()

    def selectByUP(self, phone, password):
        cond = "phone_num=%s and password=%s";
        sql = self.defaultSelectSql % (cond)
        b = self.db.get(sql, phone, password);
        return b

    def selectByPhone(self, username):
        cond = "phone_num = %s"
        sql = "select * from sys_user where %s" % (cond);
        return self.db.get(sql, username)

    def selecDInfoByUserID(self,user_id):
        sql ="select  a.phone_num,a.balance,a.integral,\
                a.occupation,\
                a.user_id,\
                sum(b.costTime) AS costTime,\
                sum(b.mileage)  AS mileage from u_d_history b RIGHT JOIN (\
                SELECT * FROM sys_user WHERE user_id = %s) a ON a.user_id = b.user_id"

        return self.db.get(sql, user_id)

    def recharge(self,userid,rechargeNum):
        sql = "update sys_user set balance=%s+balance where user_id = %s"
        return self.db.update(sql,rechargeNum,userid)

    def callTest(self):
        sql = "call order_bike(1000103,123)"
        return self.db.query(sql)

if __name__ == '__main__':
    dao = UserDao();
    user = User();
    user.username = "13112121212"
    user.password = "qqqq"
#     dao.add(user.__dict__)
    print dao.selectAll()
    print dao.selectByUP("15652750943", "15652750943")
    print dao.selectByPhone("15652750943")
    #print dao.selectByUsername("shuai1")
