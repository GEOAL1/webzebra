# /usr/bin/python
# coding: utf-8
from dao.IMysqlDao import IMysqlDao
from error.zebraError import *
from model.User import User


class UserDao(IMysqlDao):
    def __init__(self):
        pass

    defaultSelectSql = "select * from t_user where %s"

    def selectAll(self):
        return self.db.query(self.defaultSelectSql % "1");

    def add(self, user):
        sql = "insert into t_user(phone_num,password) values(%s,%s)";
        xid = self.db.execute(sql, user["phone"], user["password"]);
        user["id"] = xid;
        if xid > 0:
            return user;
        else:
            raise CreateUserError()


    def selecUserInfoByUid(self,user_id):
        sql = "select * from t_user where user_id = %s"
        return self.db.get(sql,user_id)

    def selectByUP(self, phone, password):
        cond = "phone_num=%s and password=%s";
        sql = self.defaultSelectSql % (cond)
        b = self.db.get(sql, phone, password);
        return b

    def selectByPhone(self, username):
        cond = "phone_num = %s"
        sql = "select * from t_user where %s" % (cond);
        return self.db.get(sql, username)


    def updatePassowordByPhone(self,phone,password):
        sql = "update t_user set password = %s where phone_num=%s"
        if self.db.execute_rowcount(sql,password,phone) <= 0:
            raise NotExistedPhoneOrSamePasswordError()

    def recharge(self,userid,rechargeNum):
        sql = "" \
            "update t_user set balance=%s+balance where user_id = %s"
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
