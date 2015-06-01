# /usr/bin/python
# coding: utf-8
from service.IService import IService


class UserService(IService):

    def getByPP(self,phone,password):
        return self.userDao.selectByUP(phone, password)


    def validatePP(self, phone, password):
        if len(phone) != 11 or len(password) < 6 or len(password) > 20:
            return False
        return True

    def getByPhone(self, phone):
        return self.userDao.selectByPhone(phone)

    def add(self, user):
        if(self.validatePP(user["phone"],user["password"]) == False):
            return 0;
        return self.userDao.add(user)


    def selecDInfoByUserID(self,userid):
        return self.userDao.selecDInfoByUserID(userid)

