app.service('bikeService', function ($rootScope, $http) {
    var service = {
        getNearBike: function ($scope, lng, lat) {
            alert(22222222)
            $http({
                method: "GET",
                url: '/wx/b/nearBike',
                params: {"lng": lng, "lat": lat},
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function (data, status, headers, config) {
                if (data.errorCode === 0) {
                    $scope.nearCars = data.body
                    alert("get car near success")
                } else {
                    alert('请求附近的车失败')
                }
            }).error(function (data, status, headers, config) {
                console.log("get user error")
                alert("连接服务器失败")
            })
        }
    }
    return service
})