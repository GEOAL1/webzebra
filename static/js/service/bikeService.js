app.service('bikeService', function ($rootScope, $http) {

    SendCmd = function (url, args, callback) {
        $http({
            method: "GET",
            url:  url,
            params: args,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
            if (data.errorCode === 0) {
                callback(data.errorCode,data)
                console.log("bike ctrl " + cmd + " success")
            } else {
                callback(data.errorCode,"")
                console.log(data.errMsg)
            }
        }).error(function (data, status, headers, config) {
            console.log("get user error")
            alert("连接服务器失败")
        })
    }

    var service = {
        bikeVoice: function (bike, $event) {
            SendCmd('/wx/b/ctrl/' +"voice", {bikeID: bike.id}, function (state,data) {
                if(state == 0) {
                    alert("响铃发送成功")
                }else{
                    alert("响玲发送失败")
                }
            })
            $event.preventDefault();
        },

        bikeLight: function (bike, $event) {
            SendCmd('/wx/b/ctrl/' +"light", {bikeID: bike.id}, function () {
                if(state == 0) {
                    alert("灯光发送成功")
                }else{
                    alert("灯光发送失败")
                }            })
            $event.preventDefault();
        },

        bikeOrder: function (bike, $event) {
            SendCmd('/wx/b/' + "order", {bikeID: bike.id}, function () {
                if(state == 0) {
                    alert("订购车成功")
                }else{
                    alert("订购车失败")
                }            })
            location.href = "bikeInfo.html" + bike.id
            $event.preventDefault();
        },

        bikeNavigate: function (bike, $event) {
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
            $event.preventDefault();
        },

        getNearBike: function (lng, lat, distance,callback) {
            $http({
                method: "GET",
                url: '/wx/b/nearBike',
                params: {"lng": lng, "lat": lat,"distance":distance},
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                timeout: 3000
            }).success(function (data, status, headers, config) {
                if (data.errorCode === 0) {
                    callback(0, data.body)
                } else {
                    callback(-1, {})
                    alert('请求附近的车失败')
                }
            }).error(function (data, status, headers, config) {
                console.log("get user error")
                alert("连接服务器失败")
            })
        },

        getBikeInfo: function (bikeId, callback) {
            $http({
                method: "GET",
                url: '/wx/b/info',
                params: {bikeID: bikeId},
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                timeout: 3000
            }).success(function (data, status, headers, config) {
                if (data.errorCode === 0) {
                    callback(0, data.body)
                } else {
                    callback(-1, {})
                    alert('获取车辆当前信息')
                }
            }).error(function (data, status, headers, config) {
                console.log("get bike info error")
                alert("连接服务器失败")
            })
        },
    }
    return service
})