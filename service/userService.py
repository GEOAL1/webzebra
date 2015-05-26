# /usr/bin/python
# coding: utf-8
from service.IService import IService


class UserService(IService):
    def validateUP(self, username, password):
        self.userDao.selectByUP(username, password)

    def getByUsername(self, username):
        return self.userDao.selectByUsername(username)

    def add(self, user):
        return self.userDao.add(user)
