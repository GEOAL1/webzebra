var app = angular.module('app', []);


app.directive('pwCheck', [function () {
    return {
        require: 'ngModel',
        link: function (scope, elem, attrs, ctrl) {
            var firstPassword = '#' + attrs.pwCheck;
            elem.add(firstPassword).on('blur', function () {
                scope.$apply(function () {
                    var v = elem.val() === $(firstPassword).val();
                    ctrl.$setValidity('pwCheck', v);
                });
            });
        }
    }
}]);

app.directive('uniquePhone', function ($http) {
    return {
        require: 'ngModel',
        link: function (scope, elem, attrs, ctrl) {
            elem.bind('blur', function (e) {
                scope.$apply(function () {
                    ctrl.$setValidity('uniquePhone', false);
                    phone = elem.val()
                    $http({
                        method: "GET",
                        url: '/wx/u/checkPhone/' + phone
                    }).success(function (data, status, headers, config) {
                        v = (data.errorCode === 0)
                        ctrl.$setValidity('uniquePhone', v);
                    }).error(function (data, status, headers, config) {
                        ctrl.$setValidity('uniquePhone', false);
                        console.log("无效的请求")
                    })
                });
            });
        }
    }
});