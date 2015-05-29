app.controller("panelController", function ($scope, userService, wxService, bikeService) {
    userService.getUserInfo($scope)

    getGeo(function (lng, lat) {
        $scope.lng = lng;
        $scope.lat = lat;
        bikeService.getNearBike($scope, lng, lat)
    })


    /*
     alert(JSON.parse(wxService.wx.config))
     */

    //加载折挡     //玲玲加

    //加载用户信息

    /* $scope.getNearBike = function() {
        $http({
            method: "GET",
     url: '/wx/b/list',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data, status, headers, config) {
            if (data.errorCode === 0) {
                console.log("send success");
     $scope.user=data.body
            }
        }).error(function (data, status, headers, config) {
            console.log("send error")
        })
     }



     $scope.getLocation = function(callback) {

     }*/


    //获得位置信息
    //加载附近的车
    //绑定车辆和事件
})
