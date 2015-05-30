app.controller("loginController", function ($scope, $http, userService) {
    $scope.login = userService.login
})