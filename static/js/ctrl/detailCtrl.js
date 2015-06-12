app.controller("detailController", function ($timeout, $scope, $http, userService, wxService, bikeService, geoService) {

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
        wx.scanQRCode({
            needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
            scanType: ["qrCode", "barCode"], // 可以指定扫二维码还是一维码，默认二者都有
            success: function (res) {
                var bikeid = res.resultStr; // 当needResult 为 1 时，扫码返回的结果
                $scope.bikeOrder(bikeid)
            }
        });
    }

    $scope.touchoff = function () {
        $(document).off('touchmove');
    }

    $scope.bikeLight = bikeService.bikeLight
    $scope.bikeVoice = bikeService.bikeVoice


    $scope.bikeNavigate = bikeService.bikeNavigate
    $scope.bikeOrder = bikeService.bikeOrder

    $scope.openOrderModal = function (bike) {
        $('.orderModal').fadeIn("fast")
        $scope.selectBike = bike;
        $event.preventDefault()
    }



    $scope.getBikeInfo = function (bike_id) {
        bikeService.getBikeInfo(bike_id,function(state,data) {
                if(state != 0 ){
                    alert("获取车辆信息失败，转到主页")
                    window.location.href = "/"
                }

            $scope.bike = data.body
            $scope.bike.distance = getFlatternDistance($scope.bike.latitude,$scope.bike.longitude,
                $scope.lat,$scope.lng)

                var center=new soso.maps.LatLng($scope.bike.latitude,$scope.bike.longitude);

                $scope.map=new soso.maps.Map(document.getElementById("mapContainer"),{
                    center:center,
                    zoom:15,
                })


            geoService.addMark($scope.map,$scope.lng,$scope.lat,null,
                function(mark){

                });

                geoService.addMark($scope.map,$scope.bike.longitude,$scope.bike.latitude,"img/motor5.png",
                    function(mark){
                        $scope.map.panTo(mark.getPosition())
                    });



            geoService.getAddress($scope.bike.longitude, $scope.bike.latitude, function (t, address) {
                $scope.bike.address = address
                console.log(address)
                $scope.$digest()
            })

            if($scope.bike.order_state == 1){
                $scope.bike.state = "忙碌"
            }else{
                $scope.bike.state = "可订"
            }


/*
                alert(parseInt($scope.map.getDistance(mypoint,bikepoint))+"米")
*/
        });
    }


    $scope.bike_id = GetQueryString("bike_id")

    if($scope.bike_id == null){
        alert("不合法的车辆编号")
        window.location.href = "/"
    }


    geoService.getGeo(function (status, lng, lat) {
        if (status == 0) {
            $scope.lng = lng;
            $scope.lat = lat;
        } else {
            $scope.lng = 116.397128
            $scope.lat = 39.916527
        }
        $scope.getBikeInfo($scope.bike_id )
    });

});