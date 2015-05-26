from dao.UserDao import UserDao


class IService(object):
    def __init__(self):
        self.userDao = UserDao();

    pass
