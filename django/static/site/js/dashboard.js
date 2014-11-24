
$( window ).ready( function(){

	var viewportWidth = $(document).width();
	var viewportHeight = $(document).height();
	// var column1 = $(".column1").height();
	// alert(viewportHeight);
	var formBtn = (viewportHeight - 200) / 16 - 2;
	var formBtn1 = viewportHeight - 70 - 140 - 233 * 4;
	// alert(formBtn1);
	// var formBtn1 = (viewportHeight - 210 - 233 ) / 32;
	var countriesPadding = (viewportHeight - 200) / 12 + 10;

	$(".formBox").css("width", viewportWidth - 282 + "px");

	$(".formBtn").css("paddingTop", formBtn + "px");
	$(".formBtn").css("paddingBottom", formBtn + "px");
	// alert(column1);
	$(".formBtn1").css("paddingTop", 5 + "px");
	$(".formBtn1").css("paddingBottom", 5 + "px");

	$(".countries").css("paddingTop", countriesPadding + "px");
	$(".countries").css("paddingBottom", countriesPadding + "px");

	$(".warning").css("marginTop", countriesPadding  + "px");

	$(".column3").css("height", viewportHeight + "px");
	$("#selectCountry").css("marginTop", (viewportHeight - 240)/2 + "px");
	$(".lowPoints").css("marginTop", countriesPadding - 20 + "px");

	$(".column25").css("height", viewportHeight - 70 + "px");

	$(".selectAustralia").click(function(){
		$("#selectCountry").css("display", "none");
		$(this).addClass("whiteBg");
		$(".column3").css("backgroundColor", "white");
		$(".australiaSelect").css("display", "block");
		$(".canadaSelect,.newzealandSelect").css("display", "none");
		$(".selectCanada,.selectNewZealand").removeClass("whiteBg");
	});

	$(".selectCanada").click(function(){
		$("#selectCountry").css("display", "none");
		$(this).addClass("whiteBg");
		$(".column3").css("backgroundColor", "white");
		$(".canadaSelect").css("display", "block");
		$(".australiaSelect,.newzealandSelect").css("display", "none");
		$(".selectAustralia,.selectNewZealand").removeClass("whiteBg");
	});

	$(".selectNewZealand").click(function(){
		$("#selectCountry").css("display", "none");
		$(this).addClass("whiteBg");
		$(".column3").css("backgroundColor", "white");
		$(".newzealandSelect").css("display", "block");
		$(".australiaSelect,.canadaSelect").css("display", "none");
		$(".selectCanada,.selectAustralia").removeClass("whiteBg");
	});
	
});