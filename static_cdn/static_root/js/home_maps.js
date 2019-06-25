var map;
var position;
var marker;
var infoWindow;

function loadData(map){
  var locations = [
    {lat: 19.140546, lng: 72.807055},
    {lat: 19.139951, lng: 72.808204},
    {lat: 19.139939, lng: 72.810487},
    {lat: 19.142084, lng: 72.809990}
  ]
  var others = [];
  var myself;
  var contentString;
  $.ajax({
    url: '/people/',
    method: 'GET',
    success: function(data) {
      var infoWindow = new google.maps.InfoWindow();
      for(var i = 0; i < data.others.length; i++) {
        contentString = data.others[i].contentString
        var mk = new google.maps.Marker({
          position: data.others[i].location,
          map: map
        });
        google.maps.event.addListener(mk,'click', (function(mk,contentString,infoWindow){
        return function() {
           infoWindow.setContent(contentString);
           infoWindow.open(map,mk);
        };
      })(mk,contentString,infoWindow));
      }
    },
    error: function(errorData) {
      console.log(errorData)
    }
  });

}

function initMap() {
  latlong = {lat: 19.384062, lng: 72.828551};
  map = new google.maps.Map(
    document.getElementById('map'),
    {
      center: latlong,
      zoom: 16
    }
  );
  // infoWindow = new google.maps.InfoWindow;

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      latlong = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      $.ajax({
        url: '/updateLatLong/',
        method: 'POST',
        data: latlong,
        success: function(data) {
          console.log("Success")
        },
        error: function(errorData) {
          console.log(errorData)
        }
      });

      map.setCenter(latlong);
      marker = new google.maps.Marker({
        position: latlong,
        map: map,
        icon: {
          path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
          scale: 5
        },
      });
      loadData(map);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
  // marker = new google.maps.Marker({
  //   position: latlong,
  //   map: map,
  //   icon: {
  //     path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
  //     scale: 5
  //   },
  // });
  loadData(map);
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  // infoWindow.setPosition(pos);
  // infoWindow.setContent(browserHasGeolocation ?
  //                       'Error: The Geolocation service failed.' :
  //                       'Error: Your browser doesn\'t support geolocation.');
  // infoWindow.open(map);
}
