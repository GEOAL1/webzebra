# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import random

from handle.baseHandle import BaseHandler
from model.jsonTemplate import JsonTemplate


class NearBikeHandler(BaseHandler):
    def get(self):
        try:
            lng = float(self.get_argument("lng"))
            lat = float(self.get_argument("lat"))

            body = [
                {'id': "06580", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06581", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06582", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06583", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06584", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06585", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06586", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06587", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06588", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
                {'id': "06589", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
                 'lng': lng + random.uniform(0.001, 0.000),
                 'lat': lat + random.uniform(0.001, 0.000)},
            ]
            self.write(JsonTemplate.newJsonRes().setBody(body).toJson())
        except Exception as e:
            self.write(JsonTemplate.newErrorJsonRes().setBody("error argument").toJson())
        pass


if __name__ == '__main__':
    lat = 10
    lng = float("11")

    body = [
        {'id': "06580", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06581", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06582", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06583", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06584", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06585", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06586", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06587", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06588", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
        {'id': "06589", 'price': 12, 'distance': 222, 'remainPower': 50, 'reserveKm': 5000,
         'lng': lng + random.uniform(0.001, 0.000),
         'lat': lat + random.uniform(0.001, 0.000)},
    ]

    print body
