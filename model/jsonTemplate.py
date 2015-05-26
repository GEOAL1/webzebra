# /usr/bin/python
# coding: utf-8
import json

from enum import Enum


class ErrorCode(Enum):
    success = 0
    error = 1


class JsonTemplate:
    def __init__(self):
        self.errorCode = ErrorCode.success
        pass

    errorCode = ErrorCode.success
    errorMeg = ""
    body = None;

    @staticmethod
    def newJsonRes():
        return JsonTemplate()

    @staticmethod
    def newErrorJsonRes():
        return JsonTemplate().setErrorCode(ErrorCode.error)

    def setBody(self, body):
        self.body = body
        return self;

    def setErrMsg(self, msg):
        self.errorMeg = msg;
        return self;

    def setErrorCode(self, code):
        self.errorCode = code;
        return self;

    def toJson(self):
        return json.dumps(self.__dict__)
