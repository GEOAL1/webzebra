app.controller("panelController", function ($scope, userService, wxService, bikeService, geoService) {
    $scope.search = {
        distance: 5000,
        bike_id: ""
    }

    $scope.searchBike = function () {
        $scope.getNearBike()
        $('.searchModal').fadeOut('fast')
    }


    $scope.touchon = function () {
        $(document).on('touchmove', function (e) {
            e.preventDefault();
        });
    }

    $scope.QRScanOrder = function () {
        wxService.qrScan(function(bikeid) {
            $scope.bikeOrder(bikeid)
        })
    }

    $scope.touchoff = function () {
        $(document).off('touchmove');
    }

    $scope.openBikeLV = function (bike) {
        bikeService.bikeLight(bike)
        bikeService.bikeVoice(bike)
    }

    $scope.bikeNavigate = bikeService.bikeNavigate
    $scope.bikeOrder = bikeService.bikeOrder

    $scope.openOrderModal = function (bike) {
        $('.orderModal').fadeIn("fast")
        $scope.selectBike = bike;
        $event.preventDefault()
    }


    userService.getUserInfo(function (status, data) {
        $scope.user_load_ok = true

        if (status === 0) {
            $scope.user = data.body;
            $scope.user.valibleMileage = bikeService.calValiableMileage( $scope.user.balance)
            $scope.user.valibleTime = bikeService.calValibleTime($scope.user.balance)

        } else {
            alert("获得用户信息失败，正在重新加载")
            window.location.href = "/"
        }
    })

    $scope.getNearBike = function () {
        $scope.touchon()
        $scope.user_load_ok = false

        bikeService.getNearBike($scope.lng, $scope.lat, $scope.search, function (status, data) {
            if (status == 0) {
                $scope.nearCars = data.body
                $scope.nearCars.forEach(function (bike) {
                    geoService.getAddress(bike.longitude, bike.latitude, function (t, address) {
                        bike.address = address
                        console.log(address)
                        $scope.$digest()
                    })
                })

            }
            else {
                alert("获得附近的车失败")
            }
            $scope.touchoff()
            $scope.user_load_ok = true


        })
    }

    retryGeoNum = 0;
    $scope.init =  function() {
        geoService.getGeo(function (status, lng, lat) {
            if (status == 0) {
                $scope.lng = lng;
                $scope.lat = lat;
            } else {
                if(retryGeoNum < 1) {
                    $scope.init()
                    retryGeoNum++
                }
                $scope.lng = 116.397128
                $scope.lat = 39.916527
            }
            $scope.getNearBike()

        });
    }

    $scope.init()

})

