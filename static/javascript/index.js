function searchHospitals(city) {

    $.get("/hospitals/", {hospital_name: city}, function(data){
        console.log(data);
    });
    
    // Prevent the form from submitting and refreshing the page
    return false;
}

let map;

async function initMap() {
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        // TODO: Implement search functionality using the current location and/or the location input
        map = new Map(document.getElementById("map"), {
            center: { lat: position.coords.latitude, lng:  position.coords.longitude },
            zoom: 10,
          });
    }, function() {
        alert("Could not get your current location.");
    });
} else {
    alert("Geolocation is not supported by this browser.");
}  
}

initMap();