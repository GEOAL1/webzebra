app.controller("bikeInfoController", function ($scope, $http, userService, wxService, bikeService, geoService) {

    $scope.getBikeInfo = function (bike_id) {
        bikeService.getBikeInfo(bike_id,function(state,data){
            if(state == 0) {
                $scope.bike = data;
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

    $scope.findBike = function (bike, $event) {
        bikeService.bikeLight(bike, $event)
        bikeService.bikeVoice(bike, $event)
    }


    $scope.changeBattle = function (bike, $evnet) {
        alert("changBattle")
    }


    $scope.lockBike = function (bike, $evnet) {
        alert("lockBike")
    }

    $scope.callUs = function (bike, $evnet) {
        alert("callUs")
    }

    $scope.navigate = function (bike, $evnet) {
        alert("navigate")
    }

    $scope.orderID = GetQueryString("order_id")
    if($scope.orderID == null) {
        alert("无效的订单")
        window.location.href = "/static/panel.html"
    }else{
        bikeService.getOrderByOrderID($scope.orderID,function(state,data){
            if(state == 0) {
                $scope.order = data
                $scope.getBikeInfo(data.bike_id)
            }else{
                alert("出错了")
            }
        })
    }

    $scope.finishOrderBike = function () {
        bikeService.finishOrder($scope.orderID,function(state,data){

        })
    }
})