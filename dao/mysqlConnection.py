#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function
from tornado_mysql import pools
import time
pools.DEBUG = True


class Singleton(object):  
   
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
            
        return cls._instance  
    def __init__(self,dbname,host,port,user,passwd):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.POOL = pools.Pool(
                dict(host=host, port=port, user=user, passwd=passwd, db=dbname),
                max_idle_connections=2,
                max_recycle_sec=3,
                max_open_connections=15,
            )
    def getInstance(self):
        return self.POOL
    
if __name__ == '__main__':  
    a = Singleton('gmanagernew',"10.111.32.95",3306,'root',"root")
    b = Singleton('gmanagernew',"10.111.32.95",3306,'root',"root")
    print(id(a))
    print(id(b))
    
    for i in range(10):
        c =  b.getInstance().execute("select * from sys_client")
        print(c.value)
        
    
    time.sleep(1000000)

