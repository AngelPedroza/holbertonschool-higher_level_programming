const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url).then(function(response) {
  return response.json();
}).then(function(myJson) {
  const name = myJson["name"];
  $("DIV#character").text(name);
});
