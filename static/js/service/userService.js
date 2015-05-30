app.service('userService', function ($rootScope, $http) {
    var service = {
        getUserInfo: function ($scope) {
            $scope.user_load_ok = false
            $http({
                method: "GET",
                url: '/wx/u/info',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function (data, status, headers, config) {
                if (data.errorCode === 0) {
                    $scope.user = data.body
                    $scope.user_load_ok = true
                }
            }).error(function (data, status, headers, config) {
                console.log("get user error")
                alert(status)
            })
        }
    }
    return service
})
