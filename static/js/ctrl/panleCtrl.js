app.controller("panelController", function ($scope, userService, wxService, bikeService) {

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

    userService.getUserInfo($scope)

    getGeo(function (lng, lat) {
        $scope.lng = lng;
        $scope.lat = lat;
        bikeService.getNearBike($scope, lng, lat)
    });

})
