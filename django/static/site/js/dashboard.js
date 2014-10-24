
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
		$(".canadaSelect,.japanSelect").css("display", "none");
		$(".selectCanada,.selectJapan").removeClass("whiteBg");
	});

	$(".selectCanada").click(function(){
		$("#selectCountry").css("display", "none");
		$(this).addClass("whiteBg");
		$(".column3").css("backgroundColor", "white");
		$(".canadaSelect").css("display", "block");
		$(".australiaSelect,.japanSelect").css("display", "none");
		$(".selectAustralia,.selectJapan").removeClass("whiteBg");
	});

	$(".selectJapan").click(function(){
		$("#selectCountry").css("display", "none");
		$(this).addClass("whiteBg");
		$(".column3").css("backgroundColor", "white");
		$(".japanSelect").css("display", "block");
		$(".australiaSelect,.canadaSelect").css("display", "none");
		$(".selectCanada,.selectAustralia").removeClass("whiteBg");
	});

	// $("select").onChange(function(){
	// 	$("select option").css("color","#F00");
	// });

	
});

// var whichCountry = '
// 	<div class="which-country">
// 				<a href="javascript:void(0);" class="closeBtn"></a>
// 			<span style="font-size: 14px;color:#888888;display:block;">&nbsp;&nbsp;&nbsp;Which country?</span>
// 			<div class="break10"></div>
// 			<div class="select-style">
// 			  <select>
// 			    <option value="Brazil">Brazil</option>
// 			  </select>
// 			</div>
				
// 			</div>
// 	';

// 	$(".addAnother").click(function(){
// 		// alert("append!");
// 		$("#whichCountries").append("<div class='which-country'><a href='javascript:void(0);' class='closeBtn'></a><span style='font-size: 14px;color:#888888;display:block;'>&nbsp;&nbsp;&nbsp;Which country?</span><div class='break10'></div><div class='select-style'><select><option value='Brazil'>Brazil</option></select></div></div>");
// // 		$("#whichCountries").append(whichCountry);
// 	});
// 	$(".closeBtn").click(function(){
// 		alert("close!");
// 	});
