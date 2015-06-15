app.service('wxService', function ($rootScope, $http) {
    $http({
        method: "GET",
        url: '/wx/service/get_js_config',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    }).success(function (data, status, headers, config) {
        if (data.errorCode === 0) {
            wx.config(data.body)
        }
    }).error(function (data, status, headers, config) {
        alert("请求微信配制失败")
    })


    var service = {
        isWeixinClient: function () {
            if ("micromessenger" == ua.match(/MicroMessenger/i)) {
                return true
            } else {
                return false
            }
        },

        qrScan : function (callback) {
        wx.scanQRCode({
            needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
            scanType: ["qrCode", "barCode"], // 可以指定扫二维码还是一维码，默认二者都有
            success: function (res) {
                callback(res.resultStr)
            }
        });
    }
    }

    return service
})