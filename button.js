// func that can access the user's location
function getLocation() {
    //check the user's browser support geolocation
    if (navigator.geolocation) {
      // get the user's location
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      // if unsupport, alert
      alert("Your browser does not support geolocation");
    }
  }
  
  // display the user's location
  function showPosition(position) {
    // get the user's latitude and longitude
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    // display the user's location
    document.getElementById("location").innerHTML = "Your location is: latitude " + lat + ", longitude " + lon;
  }
  