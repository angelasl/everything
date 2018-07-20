// My Variables

var map;
var ourLoc;
var view;

// Intialize a function
function init(){
  ourLoc = ol.proj.fromLonLat([-84.3869,33.7739]);

  view = new ol.View({
    center: ourLoc,
    zoom: 15 // You can change this value for aesthetics
  });

  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

window.onload = init;
