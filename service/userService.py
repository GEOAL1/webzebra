# /usr/bin/python
# coding: utf-8
from service.IService import IService


class UserService(IService):

    def getByUP(self,username,password):
        return self.userDao.selectByUP(username, password)


    def validateUP(self, username, password):
        if len(username) < 6 or len(password) < 6 or len(password) > 20 or len(username) > 20:
            return False
        return True

    def getByUsername(self, username):
        return self.userDao.selectByUsername(username)

    def add(self, user):
        if(self.validateUP(user["username"],user["password"]) == False):
            return 0;
        return self.userDao.add(user)

