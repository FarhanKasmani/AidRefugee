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
      console.log(data)
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
  latlong = {lat: 19.7514798, lng: 75.7138884};
  map = new google.maps.Map(
    document.getElementById('map'),
    {
      center: latlong,
      zoom: 13
    }
  );
  // infoWindow = new google.maps.InfoWindow;
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
