/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Menu
4. Init Isotope


******************************/

$(document).ready(function()
{
	// "use strict";

	/* 

	1. Vars and Inits

	*/

	var header = $('.header');

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();

		setTimeout(function()
		{
			$(window).trigger('resize.px.parallax');
		}, 375);
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});

	initMenu();
	// initIsotope();

	/* 

	2. Set Header

	*/

	function setHeader()
	{
		if($(window).scrollTop() > 91)
		{
			header.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
		}
	}

	/* 

	3. Init Menu

	*/

	function initMenu()
	{
		if($('.menu').length)
		{
			var header = $('.header');
			var hOverlay = $('.header_overlay');
			var menu = $('.menu');
			var hamb = $('.hamburger');
			var sup = $('.super_container_inner');
			var close = $('.menu_close');
			var overlay = $('.super_overlay');

			hamb.on('click', function()
			{
				header.toggleClass('active');
				sup.toggleClass('active');
				menu.toggleClass('active');
			});

			close.on('click', function()
			{
				header.toggleClass('active');
				sup.toggleClass('active');
				menu.toggleClass('active');
			});

			overlay.on('click', function()
			{
				header.toggleClass('active');
				sup.toggleClass('active');
				menu.toggleClass('active');
			});

			hOverlay.on('click', function()
			{
				header.toggleClass('active');
				sup.toggleClass('active');
				menu.toggleClass('active');
			});
		}
	}

	/* 

	4. Init Isotope

	*/

	// function initIsotope()
	// {
	// 	if($('.grid').length)
	// 	{
	// 		var grid = $('.grid').isotope({
	// 		  // options...
	// 		  itemSelector: '.grid-item',
	// 		  masonry: {
	// 		    columnWidth: 200
	// 		  }
	// 		});
			
	// 		// Filtering
	// 		var checkboxes =  $('.listing_checkbox label input');
	//         checkboxes.on('click', function()
	//         {
	//         	var checked = checkboxes.filter(':checked');
	//         	var filters = [];
	//         	checked.each(function()
	//         	{
	//         		var filterValue = $(this).attr('data-filter');
	//         		filters.push(filterValue);
	//         	});
		
	//         	filters = filters.join(', ');
	        	
	//         	// 같은 이유
	//         	grid.isotope({filter: filters});
	//         });
	// 	}
	// }

});
