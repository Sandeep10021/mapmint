// JavaScript Document

// INPUT ONCLICK SCRIPT-->
function clearText(field){
	if (field.defaultValue == field.value) {
		field.value = '';
	} else if (field.value == '') {
		field.value = field.defaultValue;
}
}


// on browser resize functions
// window.onresize = adjustY;

function adjustY(){
  // text vertical align middle
  $(".midalign").parent().each(function(){
	var itemH = $(this).height();
	var txtH = $(this).find('.midalign').height();
	var padTop = (itemH - txtH)/2 -1;
	if (padTop > 0) {
	  $(this).find('.midalign').css('padding-top', padTop);
	}
  });
  // mainnav: calculate right shadow height
  var mnavH = $(".mainnav ul").height();
  var mnavrshadH = mnavH + 1;
  $(".mainnav .shadrght").css('height', mnavrshadH);
  
}


// sidebar height based on maincol
function sidebarResize(){
  if ($(".sidebar").length) {
	  var sidebarH = $(".sidebar").outerHeight(true);
	  // var leafH = $(".sidebar .leaf").height();
	  var maincolH = $(".maincol").outerHeight();
	  var mainnavH = $(".mainnav").outerHeight(true);
	  // alert (sidebarH);
	  // alert (maincolH);
	  if (mainnavH > 38) {
		  var leftHcombined = sidebarH + mainnavH - 50;
	  } else {
		  var leftHcombined = sidebarH - 50;
	  }
	  if (maincolH < leftHcombined) {
		  $(".sidebar .leaf").addClass("short");
	  } /*else {
		  $(".sidebar .leaf").removeClass("short");
	  }*/
	  
	  /*if ($(window).width() > 480) {
		  var wrapperH = $("#main .wrapper").height();
		  var mainnavOuterH = $(".mainnav").outerHeight(true);
		  var leafCalcH = wrapperH - mainnavOuterH;
		  $(".sidebar .leaf").css("min-height", leafCalcH);
	  }*/
	  
	  // attempt 1
	  /*var leafTotalH = $(".sidebar .leaf").innerHeight();
	  var leafH = $(".sidebar .leaf").height();
	  var leafPad = leafTotalH - leafH;
	  var leafCalcH = maincolH - leafPad;
	  var leafMinH = parseInt($('.sidebar .leaf').css('min-height'), 10);
	  if ($("#main").width() >= 780 && leafCalcH > leafMinH) {
		  $(".sidebar .leaf").css("min-height", leafCalcH);
	  } else if ($("#main").width() < 780 && $("#main").width() > 480) {
		  var mainnavOuterH = $(".mainnav").outerHeight(true);
		  var leafCalcH780 = maincolH - mainnavOuterH - leafPad;
		  $(".sidebar .leaf").css("min-height", leafCalcH780);
	  }*/
	  
	  // attempt 3
	  /*var maincolH = $(".maincol").innerHeight();
	  var sidebarH = $(".sidebar").innerHeight();
	  var leafTotalH = $(".sidebar .leaf").innerHeight();
	  var leafH = $(".sidebar .leaf").height();
	  var leafPad = leafTotalH - leafH;
	  var leafCalcH = maincolH - leafPad;
	  if (maincolH > sidebarH) {
		  $(".sidebar .leaf").css("min-height", leafCalcH);
	  }*/
	  
  }
}


$(document).ready(function(){
	
	// FANCYBOX
	if ($('.zoom1').length) {
	  $(".zoom1").fancybox({
		  titlePosition			: 'inside',
		  'hideOnContentClick'	: false,
		  'hideOnOverlayClick'	: true,
		  'centerOnScroll'      : true
	  });
	}
	if ($(".page").length) {
		$('.page').fancybox({
		  'width'				: '75%',
		  'height'				: '75%',
		  'autoScale'     		: false,
		  'type'				: 'iframe',
		  'centerOnScroll'		: true,
		  'hideOnOverlayClick'	: false,
		  'onComplete'			: function() {
			  setTimeout(function() {
				// popup form: vertical align center
				var iframe = $('#fancybox-frame');
				if ($('.valignmid', iframe.contents()).length) {
					$('.valignmid', iframe.contents()).each(function(){
					  var iframeH = iframe.height();
					  // alert (iframeH);
					  var itemH = $('.valignmid', iframe.contents()).height();
					  // alert (itemH);
					  var padTop = (iframeH - itemH)/2;
					  if (padTop > 0) {
						$(this).css('padding-top', padTop);
					  }
				  });
				}
			  }, 200);
			}
		});
	}

	if ($(".alert").length) {
	  $('.alert').fancybox({
		  'transitionIn' : 'fade',
		  'transitionOut' : 'fade',
		  'centerOnScroll' : true,
		  'overlayShow' :	true
	  });
	}
	
	
	// mainnav functions
	if ($(".mainnav a").length) {
		
		$(".mainnav li:first").addClass('first');
		
		// insert shadow divs
		$(".mainnav ul").after('<div class="shadrght" /><div class="shadbot" />');
		
		// split words
		$(".mainnav a").splitWords();
		// $('.mainnav a.splitwords').splitWords(); // Split these words equally
		// $('.mainnav a.splitwords').splitWords(1); // Split these after the first word
		// $('.mainnav a.splitwords').splitWords(-2); // Split these after the second last word
		
		// insert vertical align span
		$(".mainnav a").wrapInner('<span class="midalign" />');
		// text vertical align middle
		// adjustY();
		
		// mouseover
		$(".mainnav a")/*.not(".current")*/.hover(function(){
			$(this).stop(true, true).animate({backgroundPosition: "0 0"}, 250);
		},function(){
			$(this).stop(true, true).animate({backgroundPosition: "0 -612px"}, 250);
		});
		
	}
	
	
	// usermenu functions
	if ($(".usermenu").length) {
		$(".usermenu a").prepend('<span class="icon" />');
		$(".usermenu li:first").addClass('first');
		$('.usermenu > li:not(:has(a))').each(function(){
			$(this).addClass('nolink');
		});
	}
	
	
	// footer functions
	if ($("#footer").length) {
		// shadow
		$("#footer").prepend('<div class="shad" />');
		// insert vertical align span
		$("#footer .btns a").wrapInner('<span class="midalign" />');
		// text vertical align middle
		// adjustY();
	}
	
	
	// panel functions
	if ($(".content .panel").length) {
		$(".content .panel li a").prepend('<span class="icon" />');
		// insert vertical align span
		$(".content .panel li").wrapInner('<span class="midalign" />');
		// text vertical align middle
		// adjustY();
	}
	
	
	// iconset1
	if ($(".btnset1 a").length) {
		$(".btnset1 a").prepend('<span class="icon" />');
		// insert vertical align span
		$(".btnset1 a span").wrapInner('<span class="midalign" />');
		// text vertical align middle
		// adjustY();
	}
	
	
	// formgen functions
	/*if ($(".formgen .wrap").length) {
		$(".formgen .wrap input:last-child, .formgen .wrap select:last-child").addClass('last');
	}*/
	if ($('.editlist').length) {
		/*$('.editlist input').wrap('<div class="base" />');
		$('.editlist .base').prepend('<div class="options" ><a class="edit">επεξεργασία</a><a class="delete">διαγραφή</a></div>');*/
		// add icons to buttons
		$('.btn1').prepend('<span />');
		// show/hide input btns
		$('.editlist .options').hover(function(){
			$(this).children('li').stop(true, true).fadeIn(200);
			// $(this).find('span').stop(true, true).fadeIn(250);
		},function(){
			$(this).children('li').stop(true, true).fadeOut(200);
			// $(this).find('span').stop(true, true).fadeOut(250);
		});
		// show input btns on click for touch devices
		$('.editlist .options').click(function(){
			$(this).children('li').fadeIn(250);
		});
		// remove field
		$('.editlist .delete').click(function(){
			$(this).closest('.base').remove();
		});
		// edit field
		$('.editlist .edit').click(function(){
			$(this).parent('.options').next('input').prop('disabled', false).focus();
			$(this).parent('.options').hide();
		});
		// lock field on blur
		$('.editlist input').blur(function(){
			$(this).prev('.options').css('display', 'block');
			$(this).prev('.options').children('li').css('display', 'none');
			$(this).prop('disabled', true);
		});
		// add field
		$('.editlist .add').click(function(){
			$(this).before('<div class="base"><input name="add_field" type="text"></div>');
			$(this).prev().find('input').focus();
		});
		
		// change hover to tap for touch devices
		/*$('.editlist .options').live("touchstart",function(e){
			var $link_id = $(this).attr('id');
			if ($(this).parent().data('clicked') == $link_id) {
				// element has been tapped (hovered), reset 'clicked' data flag on parent element and return true (activating the link)
				$(this).parent().data('clicked', null);
				return true;
			} else {
				$(this).trigger("mouseenter").siblings().trigger("mouseout"); //triggers the hover state on the tapped link (because preventDefault(); breaks this) and untriggers the hover state for all other links in the container.
				// element has not been tapped (hovered) yet, set 'clicked' data flag on parent element to id of clicked link, and prevent click
				e.preventDefault(); // return false; on the end of this else statement would do the same
				$(this).parent().data('clicked', $link_id); //set this link's ID as the last tapped link ('clicked')
			}
		});*/
		
	}
	
	// on/off switch
	if ($("input.switchbtn").length) {
	  $("input.switchbtn").switchButton({
		  on_label: "ΝΑΙ",
		  off_label: "ΟΧΙ",
		  labels_placement: "right",
		  width: 55,
		  height: 25,
		  button_width: 28
	  });
	  
	  // test if input gets checked
	  /*$("#testklik").click(function(){
		  if ($("#testattr").is(':checked')){
			  alert ("check!");
		  }
	  });*/
	}
	
	adjustY();
	
	
});

// after content is loaded
$(window).load(function () {
	
	adjustY();
	sidebarResize();
	
});


$( window ).resize(function() {
	$(".sidebar .leaf").removeClass("short");
	adjustY();
	sidebarResize();
});


// after ajax content is loaded
$(document).ajaxComplete(function() {
	$(".sidebar .leaf").removeClass("short");
	adjustY();
	sidebarResize();
});

