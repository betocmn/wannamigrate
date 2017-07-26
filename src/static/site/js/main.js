(function($) {

	skel.breakpoints({
		xlarge:	'(max-width: 1680px)',
		large:	'(max-width: 1280px)',
		medium:	'(max-width: 980px)',
		small:	'(max-width: 736px)',
		xsmall:	'(max-width: 480px)'
	});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Sets ups django ajax requests
			$.ajaxSetup({
				beforeSend: function(xhr, settings) {
					if (!csrf_safe_method(settings.type) && !this.crossDomain) {
						var csrftoken = get_cookie('csrftoken');
						xhr.setRequestHeader("X-CSRFToken", csrftoken);
					}
				}
			});

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 100);
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on medium.
			skel.on('+medium -medium', function() {
				$.prioritize(
					'.important\\28 medium\\29',
					skel.breakpoint('medium').active
				);
			});

		// Menu.
			$('#menu-content')
				.append('<a href="#menu-content" class="close"></a>')
				.appendTo($body)
				.panel({
					visibleClass: 'is-menu-content-visible',
					target: $body,
					delay: 500,
					hideOnClick: true,
					hideOnSwipe: true,
					resetScroll: true,
					resetForms: true,
					side: 'right'
				});
			$('#menu-account')
				.append('<a href="#menu-account" class="close"></a>')
				.appendTo($body)
				.panel({
					visibleClass: 'is-menu-account-visible',
					target: $body,
					delay: 500,
					hideOnClick: true,
					hideOnSwipe: true,
					resetScroll: true,
					resetForms: true,
					side: 'right'
				});

		// Banner.
			var $banner = $('#banner'),
				$header = $('#header');

			if ($banner.length > 0) {

				// Video check.
					var video = $banner.data('video');

					if (video)
						$window.on('load.banner', function() {

							// Disable banner load event (so it doesn't fire again).
								$window.off('load.banner');

							// Append video if supported.
								if (!skel.vars.mobile
								&&	!skel.breakpoint('large').active
								&&	skel.vars.IEVersion > 9)
									$banner.append('<video autoplay loop><source src="' + video + '.mp4" type="video/mp4" /><source src="' + video + '.webm" type="video/webm" /></video>');

						});

				// IE: Height fix.
					if (skel.vars.browser == 'ie'
					&&	skel.vars.IEVersion > 9) {

						skel.on('-small !small', function() {
							$banner.css('height', '100vh');
						});

						skel.on('+small', function() {
							$banner.css('height', '');
						});

					}

				// More button.
					$banner.find('.more')
						.addClass('scrolly');

				// Header.
					$header
						.addClass('with-banner')
						.addClass('alt');

					$banner.scrollex({
						mode: 'top',
						top: '-100vh',
						bottom: 10,
						enter: function() { $header.addClass('alt'); },
						leave: function() { $header.removeClass('alt'); }
					});

			}

		// Body Transparent
			var $body_transparent = $('body.transparent');
			var $header_major = $('header.major');
			if ($body_transparent.length > 0) {

				// Header.
					$header_major.scrollex({
						mode: 'top',
						top: '-100vh',
						bottom: 10,
						enter: function() { $header.addClass('alt'); },
						leave: function() { $header.removeClass('alt'); }
					});
            }


		// Spotlights.
			var $spotlight = $('.spotlight');

			if ($spotlight.length > 0
			&&	skel.canUse('transition'))
				$spotlight.each(function() {

					var $this = $(this);

					$this.scrollex({
						mode: 'middle',
						top: '-10vh',
						bottom: '-10vh',
						initialize: function() { $this.addClass('inactive'); },
						enter: function() { $this.removeClass('inactive'); }
					});

				});

		// Features.
			var $features = $('.features');

			if ($features.length > 0
			&&	skel.canUse('transition'))
				$features.each(function() {

					var $this = $(this);

					$this.scrollex({
						mode: 'middle',
						top: '-20vh',
						bottom: '-20vh',
						initialize: function() { $this.addClass('inactive'); },
						enter: function() { $this.removeClass('inactive'); }
					});

				});

		// Scrolly.
			$('.scrolly').scrolly();

		// Initial scroll.
			$window.on('load', function() {
				$window.trigger('scroll');
			});

		// Country Dropdown
			$('#country-selectize').selectize({
				maxItems: 1,
				labelField: 'name',
				valueField: 'code',
				plugins: [],
				searchField: ['name'],
				options: [{ code:"au", name:"Australia"},],
				preload: true,
				persist: false,
				render: {
					item: function(item, escape) {
						return "<div><div class='flag flag-" + escape(item.code) + "'></div><div class='name'>" + escape(item.name) + "</div></div>";
					},
					option: function(item, escape) {
						return "<div><div class='flag flag-" + escape(item.code) + "'></div><div class='name'>" + escape(item.name) + "</div></div>";
					}
				},
			});

	});

})(jQuery);
