from dao.bikeDao import BikeDao
from dao.userDao import UserDao




class IService(object):
    def __init__(self):
        self.userDao = UserDao();
        self.bikeDao = BikeDao();
        self.orderDao = OrderDao();

pass
