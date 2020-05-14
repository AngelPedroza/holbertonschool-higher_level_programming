const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url).then(function(response) {
  return response.json();
}).then(function(myJson) {
  const films = myJson["results"];
  for (let i = 0; i < films.length; i++) {
    let name = films[i]["title"];
    $("UL#list_movies").append("<li>" + name + "</li>");
  }
});
