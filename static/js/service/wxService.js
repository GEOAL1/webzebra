app.service('wxService', function ($rootScope, $http) {
    $http({
        method: "GET",
        url: '/wx/service/get_js_config',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    }).success(function (data, status, headers, config) {
        if (data.errorCode === 0) {
            wx.config(data.body)
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