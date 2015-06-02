#/usr/bin/python
#coding: utf-8
from error.zebraError import ErrorArgExpection
from service.IService import IService




class AmountService(IService):
    def recharge(self,user_id,rechargNum):
        if(rechargNum > 10000 or rechargNum < 1):
            raise ErrorArgExpection()
        return self.userDao.recharge(user_id,rechargNum)
    pass