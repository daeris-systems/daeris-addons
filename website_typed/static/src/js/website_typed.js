$('document').ready(function() {
  if (document.getElementById("typed")) {
    var typed = new Typed('#typed', {
      stringsElement: '#typed-text',
      typeSpeed: 100,
      loop: true,
    });
  }

});