$(".slide").carousel({
  interval: 2000
});
$(document).ready(function() {
  setTimeout(function() {
    $("#headText").fadeIn(300);
  }, 300);
  setTimeout(function() {
    $("#title").fadeIn(300);
  }, 400);
  setTimeout(function() {
    $("#Text").fadeIn(300);
    $("#Text2").fadeIn(300);
  }, 500);
});
