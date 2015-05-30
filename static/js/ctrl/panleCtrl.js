app.controller("panelController", function ($scope, userService, wxService, bikeService, geoService) {

    $scope.touchon = function () {
        $(document).on('touchmove', function (e) {
            e.preventDefault();
        });
    }

    $scope.touchoff = function () {
        $(document).off('touchmove');
    }

    $scope.bikeVoice = bikeService.bikeVoice
    $scope.bikeNavigate = bikeService.bikeNavigate
    $scope.bikeOrder = bikeService.bikeOrder

    $scope.user_load_ok = false

    userService.getUserInfo(function (status, user) {
        if (status === 0) {
            $scope.user = user;
            $scope.user_load_ok = true
        } else {
            alert("获得用户信息失败，正在重新加载")
            window.location.href = "/"
        }
    })

    getGeo(function (status, lng, lat) {
        if (status == 0) {
            $scope.lng = lng;
            $scope.lat = lat;
        } else {
            $scope.lng = 116.397128
            $scope.lat = 39.916527
        }
        $scope.user_load_ok = true
        $scope.touchon()
        bikeService.getNearBike($scope.lng, $scope.lat, function (status, bikes) {
            if (status == 0) {
                $scope.nearCars = bikes
                $scope.bike_load_ok = true
                $scope.touchoff()
                bikes.forEach(function (bike) {
                    geoService.getAddress(bike.lng, bike.lat, function (t, address) {
                        bike.address = address
                        console.log(address)
                        $scope.$digest()
                    })
                })
            }
            else {
                alert("获得附近的车失败")
            }


        })
        /*  }else{
         alert("获得用户坐标失败")
         }*/
    });

})
