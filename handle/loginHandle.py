#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
from handle.baseHandle import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.get_argument("name")
        self.session["user_name"] = self.get_argument("name")
        self.session.save()
        print(self.session.get("user_name")+"\n");
        self.write(r'你的session已经欧了')
        self.write(self.get_current_user());
