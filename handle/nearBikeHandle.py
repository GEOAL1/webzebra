# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class NearBikeHandler(BaseHandler):
    def get(self):
        try:
            lng = self.get_argument("lng")
            lat = self.get_argument("lat")
            body = [
                {'id': "06580", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000, 'lng': lng,
                 'lat': lat},
                {'id': "06581", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000, 'lng': lng,
                 'lat': lat},
                {'id': "06582", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000, 'lng': lng,
                 'lat': lat},
                {'id': "06583", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000, 'lng': lng,
                 'lat': lat},
                {'id': "06584", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000, 'lng': lng,
                 'lat': lat},
                {'id': "06585", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000, 'lng': lng,
                 'lat': lat},
            ]
            self.write(JsonTemplate.newJsonRes().setBody(body).toJson())
        except Exception as e:
            self.write(JsonTemplate.newErrorJsonRes().setBody("error argument").toJson())
        pass
