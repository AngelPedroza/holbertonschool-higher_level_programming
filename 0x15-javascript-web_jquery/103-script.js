window.onload = function() {
  $("INPUT#btn_translate").click(function() {
    const leng = $("INPUT#language_code").val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
    console.log(url);
    fetch(url).then(function(response) {
      return response.json();
    }).then(function(myJson) {
      $("DIV#hello").text(myJson["hello"]);
    });
  });

  $("INPUT#language_code").keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
      const leng = $("INPUT#language_code").val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + leng;
      console.log(url);
      fetch(url).then(function(response) {
	return response.json();
      }).then(function(myJson) {
	$("DIV#hello").text(myJson["hello"]);
      });
    }
  });
}
