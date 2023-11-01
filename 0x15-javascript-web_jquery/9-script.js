$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response, status) {
    if (status === 'success') {
      $('DIV#hello').text(response.hello);
    }
  });
});
