function stringFormat() {
    if (arguments.length == 0)
        return null;
    var str = arguments[0];
    for (var i = 1; i < arguments.length; i++) {
        var re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
        str = str.replace(re, arguments[i]);
    }
    return str;
}

function GetQueryString(name)
{
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if(r!=null)return  unescape(r[2]); return null;
}


function getGeo(callback) {

    var ua = navigator.userAgent.toLowerCase();

    if ("micromessenger" === ua.match(/MicroMessenger/i)) {
        wx.ready(function () {
            wx.getLocation({
                success: function (res) {
                    var latitude = res.latitude; // 纬度，浮点数，范围为90 ~ -90
                    var longitude = res.longitude; // 经度，浮点数，范围为180 ~ -180。
                    var speed = res.speed; // 速度，以米/每秒计
                    var accuracy = res.accuracy; // 位置精度
                    alert("get location from weixin success")
                    callback(0, longitude, latitude)
                },
                error: function () {
                    alert('获得地理信息失败')
                    callback(-1, "", "")
                }
            })
        })
    } else {
        var config = {enableHighAccuracy: true, timeout: 5000, maximumAge: 10000};
        navigator.geolocation.getCurrentPosition(function (position) {
            var lng = position.coords.longitude;
            var lat = position.coords.latitude;
            callback(0, lng, lat)
        }, function (error) {
            alert("获得地理信息失败")
            callback(-1, "", "")
        }, config)
    }
}

function getLocation(lat, lng, callback) {
    geocoder = new soso.maps.Geocoder();
}



