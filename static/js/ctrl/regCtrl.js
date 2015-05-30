app.controller("registerController", function ($scope,$http) {
    $scope.isloading=false
    $scope.countdown = 0
    $scope.sendCode_show=true

    $scope.sendCode = function() {
        phone = $scope.signup.phone
        $scope.countdown = 30;
        $scope.myTime = setInterval(function() {
            $scope.countdown--;
            if($scope.countdown <= 0) {
                $scope.sendCode_show=true
                clearInterval(c$sope.myTime)
            }else{
                $scope.sendCode_show=false

            }
            $scope.$digest(); // 通知视图模型的变化
        }, 1000);
        $scope.isloading=false;
        $http({
            method:"GET",
            url:'/wx/send/phoneCode?ph='+phone
        }).success(function(data,status,headers,config){
            if(data.errorCode===0) {
                console.log("send success");
            }
            alert(data.errorCode);
        }).error(function(data,status,headers,config){
            console.log("send error")
        })
    }

    $scope.signupForm = function (e) {
        alert($.param($scope.signup))
        $http({
            method:"POST",
            url:"/wx/u/reg",
            data    : $.param($scope.signup),  // pass in data as strings
            headers : { 'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (data) {
            if(data.errorCode===0) {
                alert("注册成功")
                window.location.replace("/")
            }else{
                alert("注册失败：" + data.errMsg)
            }
        }).error(function () {
            alert("请求服务器失败")
        })
    }

})


app.directive('pwCheck', [function () {
       return {
           require: 'ngModel',
                link: function (scope, elem, attrs, ctrl) {
                    var firstPassword = '#' + attrs.pwCheck;
                    elem.add(firstPassword).on('blur', function () {
                            scope.$apply(function () {
                                    var v = elem.val()===$(firstPassword).val();
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
                        method:"GET",
                        url:'/wx/u/checkPhone/'+phone
                    }).success(function(data,status,headers,config){
                        v = (data.errorCode===0)
                        ctrl.$setValidity('uniquePhone', v);
                    }).error(function(data,status,headers,config){
                        ctrl.$setValidity('uniquePhone', false);
                        console.log("无效的请求")
                    })
                });
            });
        }
    }
});
