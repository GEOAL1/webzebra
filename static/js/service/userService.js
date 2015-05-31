app.service('userService', function ($rootScope, $http) {
    var service = {
        getUserInfo: function (cb) {
            $http({
                method: "GET",
                url: '/wx/u/info',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                timeout: 3000
            }).success(function (data, status, headers, config) {

                if (data.errorCode === 0) {
                    cb(0, data.body)
                } else {
                    cb(1, "")
                }
            }).error(function (data, status, headers, config) {
                console.log("获取用户信息失败")
                cb(1, "")
            })
        },
        login: function (phone, password) {
            $.ajax({
                type: "POST",
                url: "/wx/login",
                data: $.param({"un": phone, "pw": password}),

                success: function (data1, status, headers, config) {
                    data = JSON.parse(data1)
                    if (data.errorCode === 0) {
                        window.location.href = "/"
                    } else {
                        alert("用户名密码错误")
                    }

                },
                error: function (data, status, headers, config) {
                    alert(data + status);
                }

            })
        },
        register: function (regObject) {
            $http({
                method: "POST",
                url: "/wx/u/reg",
                data: $.param(regObject),  // pass in data as strings
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function (data) {
                if (data.errorCode === 0) {
                    alert("注册成功")
                    window.location.replace("/")
                } else {
                    alert("注册失败：" + data.errMsg)
                }
            }).error(function () {
                alert("请求服务器失败")
            })
        }

    }
    return service
})
