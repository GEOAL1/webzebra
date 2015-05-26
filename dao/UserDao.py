# /usr/bin/python
# coding: utf-8
from dao.IMysqlDao import IMysqlDao
from error.zebraError import SqlError
from model.User import User


class UserDao(IMysqlDao):
    def selectAll(self):
        sql = "select * from user";
        return self.db.query(sql)

    def add(self, object):
        sql = "insert into user(username,password) values('%s','%s')" % (object.username, object.password);
        id = self.db.execute(sql, );
        object.id = id;
        if (id > 0):
            return id;
        else:
            raise SqlError("新建用户失败")

    def __selectByCondition(self, condStr):
        sql = "select * from user where %s" % condStr;
        return self.db.query(sql);

    def selectByUP(self, username, password):
        cond = "username=''"


if __name__ == '__main__':
    dao = UserDao();
    user = User();
    user.username = "shuai"
    user.password = "qqqq"
    user.state = "1";
    dao.add(user)
