window.onload = function() {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  fetch(url).then(function(response) {
    return response.json();
  }).then(function(myJson) {
    $("DIV#hello").text(myJson["hello"]);
  });
}
