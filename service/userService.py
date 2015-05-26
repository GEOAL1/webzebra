# /usr/bin/python
# coding: utf-8
from service.IService import IService


class UserService(IService):
    def validateUP(self, username, password):
        self.userDao.selectByUandP(username, password)

    def getByUsername(self, username):
        self.userDao.
        pass

    def add(self, username, password):
        pass
