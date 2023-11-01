$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + $('INPUT#language_code').val(), (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
