app.service('wxService', function ($rootScope, $http) {
    $http({
        method: "GET",
        url: '/wx/service/get_js_config',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    }).success(function (data, status, headers, config) {
        if (data.errorCode === 0) {
            wx.config({
                "timestamp": 1432973486,
                "noncestr": "1432973486.57",
                "signature": "9ba5a44ac6a2653b19e99236479bb03229dee2d7",
                "jsApiList": ["openLocation", "getLocation", "hideOptionMenu", "showOptionMenu", "hideMenuItems", "showMenuItems"],
                "appid": "wxc2b14fc7557dc863"
            })
            wx.ready(function () {
                    alert("weixin is ok")
                }
            )
            w
        }
        alert("error" + data.errMsg)
    }).error(function (data, status, headers, config) {
        alert(status)
    })


    var service = {
        isWeixinClient: function () {
            if ("micromessenger" === ua.match(/MicroMessenger/i)) {
                return true
            } else {
                return false
            }
        }
    }

    return service
})