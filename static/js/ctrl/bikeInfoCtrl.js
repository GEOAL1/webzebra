app.controller("bikeInfoController", function ($scope, $http, userService, wxService, bikeService, geoService) {

    $scope.getBikeInfo = bikeService.getBikeInfo

    $scope.bike = {
        id: 12345,
        nextOrderState: "还车",
        nextLockState: "锁车",
        isOrder: true,
        isLock: true,
        distance: 500,
        location: "东直门外大街107号",
        remainPower: 70
    }
    $scope.findBike = function (bike, $event) {
        bikeService.bikeLight(bike, $event)
        bikeService.bikeVoice(bike, $event)
    }


    $scope.orderBike = function (bike, $evnet) {
        alert("orderBike")
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


})