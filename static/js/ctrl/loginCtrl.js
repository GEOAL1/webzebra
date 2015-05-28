app.controller("loginController", function ($scope, $http) {
    $scope.login = function (e) {
        $.ajax({
            type: "POST",
            url: "/wx/login",
            data: $('#loginForm').serialize(),
            success: function (data, status, headers, config) {
                d = $.parseJSON(data)

                if (d.errorCode === 0) {
                    window.location.href = "/"
                } else {
                    alert("用户名密码错误")
                }

            },
            error: function (data, status, headers, config) {
                alert(data + status);
            }


        })
    }
})