# /usr/bin/python
# coding: utf-8


class ZebraError(StandardError):
    pass


class SqlError(ZebraError):
    pass


class ErrorArgExpection(ZebraError):
    pass
