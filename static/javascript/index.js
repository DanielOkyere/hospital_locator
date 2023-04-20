function searchHospitals() {
    // Get the location entered by the user
    var location = document.getElementById("location").value;
    
    // Get the current location of the user
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            // TODO: Implement search functionality using the current location and/or the location input
        }, function() {
            alert("Could not get your current location.");
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
    
    // Prevent the form from submitting and refreshing the page
    return false;
}