app.service('userService', function ($rootScope, $http) {
    var service = {
        getUserInfo: function ($scope) {
            $http({
                method: "GET",
                url: '/wx/u/info',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'}
            }).success(function (data, status, headers, config) {
                if (data.errorCode === 0) {
                    console.log("send success");
                    $scope.user = data.body
                }
            }).error(function (data, status, headers, config) {
                console.log("get user error")
                alert(status)
            })
        }
    }
    return service
})
