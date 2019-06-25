var map = new google.maps.Map(document.getElementById('map'),{
  center:{
    lat:9.949403,
    lng:76.258620
  },
  zoom:10
});
var marker=new google.maps.Marker({
  position:{
    lat:9.949403,
    lng:76.258620
  },
  map:map,
  draggable:true
  });


google.maps.event.addListener(marker,'dragend',function(){
  var lat=marker.getPosition().lat();
  var lng=marker.getPosition().lng();
  console.log(lat,lng);

  document.getElementById("lat").value = lat;
  document.getElementById("lon").value = lng;

});
