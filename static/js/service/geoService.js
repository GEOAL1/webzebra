app.service('geoService', function ($rootScope, $http) {

    var service = {
        getAddress: function (lng, lat, callback) {

            qq.maps.convertor.translate(new qq.maps.LatLng(lat, lng), 1, function (res) {
                var latLng = new soso.maps.LatLng(res[0].lat, res[0].lng);
                var geocoder = new soso.maps.Geocoder();

                geocoder.setComplete(function (e) {
                    callback(0, e.detail.address)
                })

                geocoder.setError(function () {
                    callback(1, "获取失几")
                    console.log("get address failed")
                })

                geocoder.getAddress(latLng)

            })
        }

    }
    return service
})
