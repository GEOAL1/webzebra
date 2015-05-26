# /usr/bin/python
# coding: utf-8
from dao.IMysqlDao import IMysqlDao
from error.zebraError import SqlError
from model.User import User


class UserDao(IMysqlDao):
    def __init__(self):
        pass

    defaultSelectSql = "select * from user where %s"

    def selectAll(self):
        return self.db.query(self.defaultSelectSql % "1");

    def add(self, user):
        sql = "insert into user(username,password) values(%s,%s)";
        id = self.db.execute(sql, user["username"], user["password"]);
        user["id"] = id;
        if id > 0:
            return user;
        else:
            raise SqlError("新建用户失败")

    def selectByUP(self, username, password):
        cond = "username=%s and password=%s";
        sql = self.defaultSelectSql % (cond)
        return self.db.query(sql, username, password);

    def selectByUsername(self, username):
        cond = "username = %s"
        sql = self.defaultSelectSql % (cond)
        return self.db.query(sql, username)


if __name__ == '__main__':
    dao = UserDao();
    user = User();
    user.username = "shuai1"
    user.password = "qqqq"
    user.state = "1";
    dao.add(user.__dict__)
    print dao.selectAll()
    print dao.selectByUP("shuai1", "qqqq")
    print dao.selectByUsername("shuai1")
