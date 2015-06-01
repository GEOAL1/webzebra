# /usr/bin/python
# coding: utf-8
from dao.IMysqlDao import IMysqlDao
from error.zebraError import SqlError
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
            raise SqlError("新建用户失败")

    def selectByUP(self, phone, password):
        cond = "phone_num=%s and password=%s";
        sql = self.defaultSelectSql % (cond)
#         return self.db.query(sql, username, password);
        b = self.db.get(sql, phone, password);
        return b

    def selectByPhone(self, username):
        cond = "phone_num = %s"
        sql = "select * from sys_user where %s" % (cond);
        return self.db.get(sql, username)

    def selecDInfoByUserID(self,user_id):
        sql ="SELECT\
                a.phone_num,\
                a.balance,\
                a.integral,\
                a.occupation,\
                a.user_id,\
                sum(b.costTime) AS costTime,\
                sum(b.mileage)  AS mileage\
                FROM sys_user a LEFT JOIN u_d_history b ON a.user_id = %s AND a.user_id = b.user_id"

        return self.db.get(sql, user_id)


if __name__ == '__main__':
    dao = UserDao();
    user = User();
    user.username = "13112121212"
    user.password = "qqqq"
#     dao.add(user.__dict__)
    #print dao.selectAll()
    print dao.selectByUP("15652750943", "15652750943")
    print dao.selectByPhone("15652750943")
    #print dao.selectByUsername("shuai1")
