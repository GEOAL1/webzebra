app.service('userService', function ($rootScope, $http) {
    var service = {
        getUserInfo: function ($scope) {
            $scope.user_load_ok = false
            $http({
                method: "GET",
                url: '/wx/u/info',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function (data, status, headers, config) {
                if (data.errorCode === 0) {
                    $scope.user = data.body
                    $scope.user_load_ok = true
                }
            }).error(function (data, status, headers, config) {
                console.log("get user error")
                alert(status)
            })
        },
        login: function (phone, password) {
            $.ajax({
                type: "POST",
                url: "/wx/login",
                data: $.param({"phone": phone, "password": password}),

                success: function (data, status, headers, config) {

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
