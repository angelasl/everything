// DECLARE VARIABLES
var ourLoc;
var view;
var map;

// the INITialize function, which starts the map on specified settings
function init() {
	// These are the coordinates of the GWC AT&T Atlanta SIP location
	ourLoc = ol.proj.fromLonLat([-84.3869,33.7739]);

	view = new ol.View({
		center: ourLoc,
		zoom: 18 // This is an aesthetically pleasing zoom value, but can be modified
	});

	map = new ol.Map({
		target: 'map',
		layers: [
		  new ol.layer.Tile({
		    source: new ol.source.OSM()
		  })
		],
		// Note from the View Animation website:
		// Improve user experience by loading tiles while animating. Will make
		// animations stutter on mobile or slow devices.
		loadTilesWhileAnimating: true,
		view: view
	});
}

// the panHome function which tells the map to return to default location
function panHome() {
	view.animate({
		center: ourLoc, // "Home" Location
		duration: 2000  // Two seconds
	});
}

// the panToCountry function which tells the map to go to specified country
// function panToCountry() {
// 	var countryName = document.getElementById("country-name").value;
//
// 	if(countryName === ""){
// 		alert("You didn't enter a country name!");
// 		return;
// 	}
//
// 	var lon = 0.0;
// 	var lat = 0.0;
//
// 	var query = "https://restcountries.eu/rest/v2/name/"+countryName
// 	// This replaces spaces with %20, which is read easily by browsers
// 	query = query.replace(/ /g, "%20")
// 	alert(query);
//
// 	// HTTP GET Request
// 	var countryRequest = new XMLHttpRequest();
// 	countryRequest.open('GET', query, false);
// 	// Send the GET request
// 	countryRequest.send();
//
//   // Show alerts for debugging
// 	// alert("Ready State " + countryRequest.readyState);
// 	// alert("Status " + countryRequest.status);
// 	// alert("Response" + countryRequest.responseText);
//
// 	if(countryRequest.readyState != 4 || countryRequest.status != 200
// 	|| countryRequest.responseText === ""){
// 		alert("Request had an error!");
// 		return;
// 	}
//
// 	var countryInformation= JSON.parse(countryRequest.responseText);
//
// lat= countryInformation[0].latlng[0];
// lon= countryInformation[0].latlng[1];
//
// alert(countryName + ": Lon " + lon + " & Lat " + lat);
//
// 	var location = ol.proj.fromLonLat([lon, lat]);
//
// 	view.animate({
// 		center: location, // Location
// 		duration: 2000  // Two seconds
// 	});
// }

function makeCountryRequest() {
	var countryName = document.getElementById("country-name").value;

	if(countryName === ""){
		alert("You didn't enter a country name!");
		return;
	}

	var query =
	"https://restcountries.eu/rest/v2/name/"+countryName+"?fullText=true"
	// This replaces spaces with %20, which is read easily by browsers
	query = query.replace(/ /g, "%20")

	// HTTP GET Request
	var countryRequest = new XMLHttpRequest();
	countryRequest.open('GET', query, true);
countryRequest.onload = processCountryRequest

	// Send the GET request
	countryRequest.send();
}

function processCountryRequest() {
	var lon = 0.0;
	var lat = 0.0;

	if(countryRequest.readyState != 4){
		return;
	}

	if(countryRequest.status != 200 || countryRequest.responseText === ""){
		alert("We were unable to find your requested country.");
		return;
	}

	var countryInformation= JSON.parse(countryRequest.responseText);

lat= countryInformation[0].latlng[0];
lon= countryInformation[0].latlng[1];

// alert(countryName + ": Lon " + lon + " & Lat " + lat);

	var location = ol.proj.fromLonLat([lon, lat]);

	view.animate({
		center: location, // Location
		duration: 2000  // Two seconds
	});
}
// Calls the init function on first load.
window.onload = init;
