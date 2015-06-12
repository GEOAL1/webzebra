app.service('bikeService', function ($rootScope, $http) {
    var sendCmd = function (url, method, data, callback) {
        var http_config = {};
        if (method == "GET") {
            http_config = {
                method: "GET",
                url: url,
                params: data,
                timeout: 10000,
            }
        } else {
            http_config = {
                method: "POST",
                url: url,
                data: $.param(data),
                timeout: 10000,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            }
        }

        $http(http_config).success(function (data, status, headers, config) {
            if (data.errorCode != 0) {
                console.log(data.errorCode + " : " + data.errorMeg);
                data.body = {};
            }
            callback(data.errorCode, data)
        }).error(function (data, status, headers, config) {
            if (status == 403) {
                alert("登录超时，请重新登录")
                window.location.href = "/static/login.html"
            }
            //alert(status + ":" + "连接服务器失败");
            callback(-1, {errorCode: -1, errorMeg: status, body: ""});
        });
    };

    var service = {
        bikeVoice: function (bike, cb) {
            sendCmd('/wx/b/ctrl/voice', "GET", {bikeID: bike.bike_id}, function (state, data) {
                if(state == 0) {
                    alert("响铃发送成功")
                }else{
                    alert("响玲发送失败")
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },

        bikeLight: function (bike, cb) {
            sendCmd('/wx/b/ctrl/light', "GET", {bikeID: bike.bike_id}, function (state, data) {
                if(state == 0) {
                    alert("灯光发送成功")
                }else{
                    alert("灯光发送失败")
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },

        lockBike: function (bike, cb) {
            var cmd;
            if (bike.lock_state == 0) {
                cmd = "lock";
            } else {
                cmd = "unlock"
            }

            sendCmd('/wx/b/ctrl/' + cmd, "GET", {bikeID: bike.bike_id}, function (state, data) {
                if(state == 0) {
                    alert("命令发送成功")
                }
            });
        },

        bikeOrder: function (bike_id, callback) {
            sendCmd('/wx/o/order', "GET", {bikeID: bike_id}, function (state, data) {
                if (state == 0) {
                    alert("订购车成功")
                    location.href = "/"
                }else{
                    alert(data.errorMeg)
                }

                if (cb != undefined) {
                    cb(state, data)
                }

            })
        },


        finishOrder: function(orderid,callback) {
            sendCmd('/wx/o/finish', "GET", {order_id: orderid}, function (state, data) {
                if(state == 0){
                    alert(data.errorMeg)

                    window.location.href="/"
                }else{
                    alert("取消失败")
                }

                if (cb != undefined) {
                    cb(state, data)
                }
            })
        },


        getOrderByOrderID: function (orderID,callback) {
            sendCmd('/wx/o/get', "GET", {order_id: orderID}, function (state, data) {
                callback(state, data)
            })
        },


        bikeNavigate: function (bike) {
            qq.maps.convertor.translate(new qq.maps.LatLng(bike.latitude, bike.longitude), 1, function (res) {
                        wx.openLocation({
                            latitude: res[0].lat,
                            longitude: res[0].lng,
                            name: "",
                            address: "",
                            scale: 27,
                            infoUrl: ""
                        })
                })
        },

        getNearBike: function (lng, lat, search, callback) {
            sendCmd('/wx/b/search', "GET", {
                "lng": lng,
                "lat": lat,
                "distance": search.distance,
                "bike_id": search.bike_id
            }, function (state, data) {
                callback(state, data)
            })
        },

        getBikeInfo: function (bikeId, callback) {
            sendCmd('/wx/b/info', "GET", {bikeID: bikeId}, function (state, data) {
                callback(state, data)
            })
        },

        calPrice:function(mileage,costTime) {
            var timePrice = costTime * 1
            var mileagePrice = 0.8 * (mileage / 1000.0) * 10
            if(timePrice < mileagePrice)
                cost = mileagePrice
            else
                cost = timePrice
            return cost
        },

        calValiableMileage:function(balance) {
            return balance
        },

        calValableTime:function(balance){
            return balance / 10.0 / 0.8 * 1000
        }


    }
    return service
})