function FSelector(pageID) {
  switch (pageID) {
    case 0:
      $("#1").fadeOut(200);
      $("#2").fadeOut(200);
      $("#3").fadeOut(200);
      $("#N" + 1).removeClass("active");
      $("#N" + 2).removeClass("active");
      $("#N" + 3).removeClass("active");
      break;
    case 1:
      $("#0").fadeOut(200);
      $("#2").fadeOut(200);
      $("#3").fadeOut(200);
      $("#N" + 0).removeClass("active");
      $("#N" + 2).removeClass("active");
      $("#N" + 3).removeClass("active");
      break;
    case 2:
      $("#0").fadeOut(200);
      $("#1").fadeOut(200);
      $("#3").fadeOut(200);
      $("#N" + 1).removeClass("active");
      $("#N" + 0).removeClass("active");
      $("#N" + 3).removeClass("active");
      break;
    case 3:
      $("#0").fadeOut(200);
      $("#1").fadeOut(200);
      $("#2").fadeOut(200);
      $("#N" + 1).removeClass("active");
      $("#N" + 2).removeClass("active");
      $("#N" + 0).removeClass("active");
      break;
    default:
      break;
  }
  setTimeout(function() {
    $("#" + pageID).fadeIn(200);
    $("#N" + pageID).addClass("active");
  }, 199);
}
