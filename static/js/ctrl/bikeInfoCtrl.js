app.controller("bikeInfoController", function ($timeout, $scope, $http, userService, wxService, bikeService, geoService) {

    $scope.user_load_ok = false

    $scope.getBikeInfo = function (bike_id) {
        bikeService.getBikeInfo(bike_id,function(state,data){
            if(state == 0) {
                $scope.bike = data.body;
                if($scope.bike.lock_state==1) {
                    $scope.bike.nextLockState = "锁车"
                    $scope.bike.curLockState="未锁"
                    $scope.lock_img = "img/lock.png"
                }else{
                    $scope.bike.nextLockState = "解锁"
                    $scope.bike.curLockState="已锁"
                    $scope.lock_img = "img/unlock.png"
                }
                $scope.order.mileage= $scope.bike.mileage - $scope.order.begin_mileage
                $scope.order.cost = bikeService.calPrice($scope.order.mileage,$scope.order.cost_time)

               $scope.order.price =  $scope.order.cost
                if($scope.order.cost < 10)
                    $scope.order.price = 10

                newbalance = $scope.user.balance - $scope.order.cost

                if(newbalance < 20 && newbalance > 5)
                    alert("您的余额不足，请注意，本次应扣出 " + $scope.order.price +
                    "斑马币,帐户可用余额 "+$scope.user.balance + "斑马币")
                else if(newbalance <= 5 && newbalance > 2 )
                    alert("可用余额不嘎，车辆即将被锁，请注意车辆停放位置")

                else if(newbalance <= 0) {
                    alert("没钱了，结束本次服务")
                    $scope.finishOrderBike()
                }
            }
            $scope.user_load_ok=true
        })
    }

    $scope.bikeLight = bikeService.bikeLight
    $scope.bikeVoice = bikeService.bikeVoice


    $scope.lockBike = function (bike) {
        bikeService.lockBike(bike,function(state,data){
            if(state == 0)
                $scope.refreshInfo()
        })
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

    var updateClock = function () {
        $scope.clock = new Date();
        $timeout(function () {
            $scope.refreshInfo()
        }, 60000);
    };


    $scope.refreshInfo = function () {
        bikeService.getOrderByOrderID($scope.orderID, function (state, data) {
            if (state == 0) {
                $scope.order = data.body
                $scope.getBikeInfo($scope.order.bike_id)
            } else {
                window.location.href = "/"
            }
        })
    }


    if($scope.orderID == null) {
        userService.getUserOrder(function (statue, data) {
            if (statue == 0) {
                $scope.orderID = data.body.order_id
                $scope.refreshInfo()
                updateClock()
            }
            else {
                alert("你还没订车,快去选车吧")
                window.location.href = "/static/panel.html"
            }
        })
    }else{
        $scope.refreshInfo()
        updateClock()
    }

    userService.getUserInfo(function (status, data) {
        $scope.user_load_ok = true

        if (status === 0) {
            $scope.user = data.body;
        } else {
            alert("获得用户信息失败，正在重新加载")
            window.location.href = "/"
        }
    })
})