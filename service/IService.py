from dao.bikeDao import BikeDao
from dao.userDao import UserDao
from dao.orderDao import OrderDao




class IService(object):
    def __init__(self):
        self.userDao = UserDao();
        self.bikeDao = BikeDao();
        self.orderDao = OrderDao();

pass
