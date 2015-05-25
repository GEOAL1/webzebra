#/usr/bin/python
# coding: utf-8
#Createtime 2015/5/25 by eric
import torndb



class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MysqlMananger(Singleton):
    db=torndb.Connection("10.111.32.61","fckb","shuai","shuai123")


if __name__ == '__main__':
    dbmanager = MysqlMananger();
    a = dbmanager.db.get("select * from t_strategy_type")
    print a