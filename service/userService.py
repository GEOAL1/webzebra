# /usr/bin/python
# coding: utf-8
from error.zebraError import ExistedPhoneError
from service.IService import IService


class UserService(IService):

    def getByPP(self,phone,password):
        return self.userDao.selectByUP(phone, password)

    def validatePP(self, phone, password):
        if len(phone) != 11 or len(password) < 6:
            return False
        return True

    def getByPhone(self, phone):
        ret = self.userDao.selectByPhone(phone)
        if(ret is not None):
            raise ExistedPhoneError()

    def add(self, user):
        if(self.validatePP(user["phone"],user["password"]) == False):
            return 0;
        return self.userDao.add(user)


    def selecUserInfoByUid(self,userid):
        return self.userDao.selecUserInfoByUid(userid)

