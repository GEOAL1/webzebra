app.controller("registerController", function ($scope) {

})



app.directive('pwCheck', [function () {
       return {
           require: 'ngModel',
                link: function (scope, elem, attrs, ctrl) {
                    var firstPassword = '#' + attrs.pwCheck;
                    elem.add(firstPassword).on('keyup', function () {
                            scope.$apply(function () {
                                    var v = elem.val()===$(firstPassword).val();
                                   ctrl.$setValidity('pwCheck', v);
                            });
                         });
                 }
         }
     }]);

app.directive('uniquePhone', [function ($http) {
    return {
        require: 'ngModel',
        link: function (scope, elem, attrs, ctrl) {
            elem.on('onBlur', function () {
                scope.$apply(function () {
                    var v = elem.val()===$(firstPassword).val();
                    $.post('/u/check/'+name).success(function(data){
                        data.error
                        ctrl.$setValidity('phoneCheck', v);
                    })
                });
            });
        }
    }
}]);
