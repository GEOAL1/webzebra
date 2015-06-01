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
        xid = self.db.execute(sql, user["username"], user["password"]);
        user["id"] = xid;
        if xid > 0:
            return user;
        else:
            raise SqlError("新建用户失败")

    def selectByUP(self, username, password):
        cond = "phone_num=%s and password=%s";
        sql = self.defaultSelectSql % (cond)
#         return self.db.query(sql, username, password);
        b = self.db.query(sql, username, password);
        return b

    def selectByUsername(self, username):
        cond = "phone_num = %s"
        sql = self.defaultSelectSql % (cond)
        return self.db.query(sql, username)


if __name__ == '__main__':
    dao = UserDao();
    user = User();
    user.username = "13112121212"
    user.password = "qqqq"
#     dao.add(user.__dict__)
    #print dao.selectAll()
    print dao.selectByUP("13112121212", "qqqq")
    print dao.selectByUsername("13112121212")
    #print dao.selectByUsername("shuai1")
