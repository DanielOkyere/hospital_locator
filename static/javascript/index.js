let map;

async function initMap() {
    //@ts-ignore
    const { Map } = await google.maps.importLibrary("maps");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            let { latitude, longitude } = position.coords;
            let youMarkerOptions = {
                position: new google.maps.LatLng(latitude, longitude),
                icon: '/imgs/you.png',
                title: 'This is your current location',
                optimized: true,
                animation: google.maps.Animation.DROP
            }
            map = new Map(document.getElementById("map"), {
                center: { lat: position.coords.latitude, lng: position.coords.longitude },
                zoom: 10,
            });
            let marker = new google.maps.Marker(youMarkerOptions);
            marker.setMap(map);
            $.get("/hospitals/", function (data) {
                let markerLocations = [];
                data.map((d) => markerLocations.push({
                    lat: d.latitude,
                    lng: d.longitude
                }))
                for (var i = 0; i < markerLocations.length; i++) {
                    var marker = new google.maps.Marker({
                        position: markerLocations[i],
                        map: map
                    });
                }
                console.log(data);
            });
        
        }, function () {
            alert("Could not get your current location.");
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

initMap();
