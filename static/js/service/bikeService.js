app.service('bikeService', function ($rootScope, $http) {

    SendCmd = function (cmd, args, callback) {
        $http({
            method: "GET",
            url: '/wx/b/ctrl/' + cmd,
            params: args,
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
            if (data.errorCode === 0) {
                callback(data)
                console.log("bike ctrl " + cmd + " success")
            } else {
                alert('cmd execute failed')
                console.log(data.errMsg)
            }
        }).error(function (data, status, headers, config) {
            console.log("get user error")
            alert("连接服务器失败")
        })
    }

    var service = {
        bikeVoice: function (car, $event) {
            SendCmd("voice", {bikeID: car.id}, function () {
                alert("声音发送成功")
            })
            $event.preventDefault();
        },

        bikeOrder: function (car, $event) {
            alert("订购编号" + "成功，跳转到控制页")
            location.href = "/static/bikeInfo.html?carid=" + car.id
            $event.preventDefault();
        },

        bikeNavigate: function (car, $event) {
            wx.getLocation({
                success: function (res) {
                    qq.maps.convertor.translate(new qq.maps.LatLng(res.latitude, res.longitude), 1, function (res) {
                        wx.openLocation({
                            latitude: res[0].lat,
                            longitude: res[0].lng,
                            name: "",
                            address: "",
                            scale: 28,
                            infoUrl: ""
                        })
                })
                }

            })


            $event.preventDefault();
        },

        getNearBike: function (lng, lat, callback) {
            $http({
                method: "GET",
                url: '/wx/b/nearBike',
                params: {"lng": lng, "lat": lat},
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
                $scope.touchoff()
            })
        }
    }
    return service
})