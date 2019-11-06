(function($) {
  <!--img area-->
  $("img").mouseenter(function () {
    $(this).parent().parent().prev().prev(".icons").children("ul").css({
      "visibility": "visible",
      "opacity":"1",
      "-webkit-transform": "translate(0, -100%)",
      "transform": "translate(0, 25%)",
      "transition":"all 0.3s ease-in-out"
    });
    $(this).parent().parent().prev(".labels").children().children("a").css({
      "visibility": "visible",
      "opacity":"1",
      "-webkit-transform": "translateY(100%)",
      "transform": "translate(0, 25%)",
      "transition":"all 0.3s ease-in-out"
    });
    $(this).mouseleave (function () {
      $(this).parent().parent().prev().prev(".icons").children("ul").css({
        "visibility": "hidden",
        "opacity":"0",
        "-moz-transform": "translateY(-100%)",
        "-webkit-transform": "translateY(-100%)",
        "-ms-transform": "translateY(-100%)",
        "transform": "translateY(-10%)",
        "-webkit-transition":"all 1s ease-in-out",
        "transition":"all 0.3s ease-in-out"
      });
    });
    $(this).mouseleave (function () {
      $(this).parent().parent().prev(".labels").children().children("a").css({
        "visibility": "hidden",
        "opacity":"0",
        "-moz-transform": "translateY(100%)",
        "-webkit-transform": "translateY(100%)",
        "-ms-transform": "translateY(100%)",
        "transform": "translateY(20px)",
        "-webkit-transition":"all 1s ease-in-out",
        "transition":"all 0.3s ease-in-out"
      });
    });
  });
  <!--icon area-->
  $("li").mouseenter(function () {
    $(this).parent(".flag").css({
      "opacity":"1",
      "visibility": "visible",
      "-webkit-transform": "translate(0, -100%)",
      "transform": "translate(0, 25%)",
      "transition":"all 0.3s ease-in-out"
    });
    $(this).parent().parent().next(".labels").children("ul").children("a").css({
      "visibility": "visible",
      "opacity":"1",
      "-webkit-transform": "translate(0, -100%)",
      "transform": "translate(0, 25%)",
      "transition":"all 0.3s ease-in-out"
    });
    $(this).mouseleave (function () {
      !$(this).parent(".flag").css({
        "visibility": "hidden",
        "opacity":"0",
        "-moz-transform": "translateY(-100%)",
        "-webkit-transform": "translateY(-100%)",
        "-ms-transform": "translateY(-100%)",
        "transform": "translateY(-10%)",
        "-webkit-transition":"all 1s ease-in-out",
        "transition":"all 0.3s ease-in-out"
      });
      $(this).parent().parent().next(".labels").children("ul").children("a").css({
        "visibility": "hidden",
        "opacity":"0",
        "-moz-transform": "translateY(100%)",
        "-webkit-transform": "translateY(100%)",
        "-ms-transform": "translateY(100%)",
        "transform": "translateY(20px)",
        "-webkit-transition":"all 1s ease-in-out",
        "transition":"all 0.3s ease-in-out"
    });
    });

  });
  <!--label area-->
  $(".KSVul").mouseenter(function () {
    $(this).children().css({
      "visibility": "visible",
      "opacity":"1",
      "-webkit-transform": "translateY(100%)",
      "transform": "translate(0, 25%)",
      "transition":"all 0.3s ease-in-out"
    });
    $(this).parent().prev(".icons").children("ul").css({
      "opacity":"1",
      "visibility": "visible",
      "-webkit-transform": "translate(0, -100%)",
      "transform": "translate(0, 25%)",
      "transition":"all 0.3s ease-in-out"
    });
    $(this).mouseleave (function () {
      !$(this).children().css({
        "visibility": "hidden",
        "opacity":"0",
        "-moz-transform": "translateY(100%)",
        "-webkit-transform": "translateY(100%)",
        "-ms-transform": "translateY(100%)",
        "transform": "translateY(20px)",
        "-webkit-transition":"all 1s ease-in-out",
        "transition":"all 0.3s ease-in-out"
      });
      $(this).parent().prev(".icons").children("ul").css({
        "visibility": "hidden",
        "opacity":"0",
        "-moz-transform": "translateY(-100%)",
        "-webkit-transform": "translateY(-100%)",
        "-ms-transform": "translateY(-100%)",
        "transform": "translateY(-10%)",
        "-webkit-transition":"all 1s ease-in-out",
        "transition":"all 0.3s ease-in-out"
    });
    });
  });
})(jQuery);
