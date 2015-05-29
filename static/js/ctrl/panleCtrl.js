app.controller("panelController", function ($cookies, $scope, $http) {
    //加载折挡
    //玲玲加

    $scope.loadUserInfo = function () {
        $http({
            method: "GET",
            url: '/wx/u/info',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
            if (data.errorCode === 0) {
                console.log("send success");
                alert(data.body)
            }
        }).error(function (data, status, headers, config) {
            console.log("send error")
        })
    }()
    //加载用户信息

    //获得位置信息
    //加载附近的车
    //绑定车辆和事件
})
