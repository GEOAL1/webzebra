app.controller("bikeInfoController", function ($scope, $http, userService, wxService, bikeService, geoService) {
    $scope.getBikeInfo = function (bike_id) {
        bikeService.getBikeInfo(bike_id,function(state,data){
            if(state == 0) {
                $scope.bike = data.body;
                if($scope.bike.lock_state==0) {
                    $scope.bike.nextLockState = "锁车"
                    $scope.bike.curLockState="未锁"
                }else{
                    $scope.bike.nextLockState = "解锁"
                    $scope.bike.curLockState="已锁"
                }
            }
        })
    }

    $scope.bikeLight = bikeService.bikeLight
    $scope.bikeVoice = bikeService.bikeVoice


    $scope.lockBike = function (bike) {
        bikeService.lockBike(bike)
    }

    $scope.callUs = function (bike) {
        alert("callUs")
    }

    $scope.navigate = function (bike) {
        bikeService.bikeNavigate(bike)
    }

    $scope.finishOrderBike = function () {
        bikeService.finishOrder($scope.orderID, function (state, data) {

        })
    }


    $scope.orderID = GetQueryString("order_id")
    if($scope.orderID == null) {
        userService.getUserOrder(function (statue, data) {
            if (statue == 0) {
                $scope.orderID = data.body.order_id
                bikeService.getOrderByOrderID($scope.orderID, function (state, data) {
                    if (state == 0) {
                        $scope.order = data.body
                        $scope.getBikeInfo($scope.order.bike_id)
                    } else {
                        alert("你还没订车")
                    }
                })
            }
            else {
                alert("你还没订车,快去选车吧")
                window.location.href = "/static/panel.html"
            }
        })
    }else{
        bikeService.getOrderByOrderID($scope.orderID,function(state,data){
            if(state == 0) {
                $scope.order = data.body
                $scope.getBikeInfo($scope.order.bike_id)
            }else{
                alert("你还没订车")
            }
        })
    }
})