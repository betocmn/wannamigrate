$(function() {
    'use strict'

    // A JS library that detects mobile devices.
    var isMobile = {
        Android: function() {
            return navigator.userAgent.match(/Android/i);
        },
        BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i);
        },
        iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i);
        },
        iPhone: function() {
            return navigator.userAgent.match(/iPhone/i);
        },
        iPad: function() {
            return navigator.userAgent.match(/iPad/i);
        },
        iPod: function() {
            return navigator.userAgent.match(/iPod/i);
        },
        Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i);
        },
        Windows: function() {
            return navigator.userAgent.match(/IEMobile/i);
        },
        any: function() {
            return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        },
        any768: function() {
            return (window.innerWidth <= 768 || isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
        }
    };

    // $scope is an object that references the elements in the implementation of the DOM structure.
    var $scope = {
        html : $('html'),
        header : $('header'),
        logo : $('.logo'),
        shadow : $('.shadow'),
        btMyAccount : $('.my-account.options'),

        nav: {
            this: $('.nav'),
            navLink: $('.nav-link'),
            btNav: $('.bt-nav')
        },

        contents: {
            home: $('.content.home')
        },

        tabs: {
            btAlternador: $('.bt-alternator'),
            tabQuestions: {
                this: $('.home-questions'),
                content: $('.content-questions')
            },
            tabProfessionals: {
                this: $('.home-professionals'),
                content: $('.content-professionals')
            }
        },

        search: {
            btSearch: $('.bt-search'),
            input: $('.search-input'),
            btBack: $('.search .bt-back')
        },

        boxOptions: {
            this : $('.box-options '),
            btCancel :  $('.bt-cancel'),
            btOptions :  $('.bt-options')
        },

        changeSituation: {
            btChange: $('.bt-change'),
            btChangeSituation: $('.bt-change-situation'),
            flag : {
                from: $('.from-flag'),
                to: $('.to-flag')
            },

            country : {
                from : $('.from-country'),
                to : $('.to-country'),
            }
        },

        situations: {
            situation: $('.situation'),
            changeSituation: $('.change-situation')
        }
    }

    // attributes
    // ---------
    var alternateTab,
        alternateShadow,
        from,
        to,
        textFrom,
        textTo

    var dashboard = {

        // Methods
        // ---------

        // Method that runs only on the mobile version
        mobile: function(){
            alternateTab = false;
            alternateShadow = false;
            dashboard.tabsDashboard.init();
            dashboard.search.init();
        },

        shadow: function(){
            if (!alternateShadow) {
                $scope.shadow.fadeIn();
                alternateShadow = true;
            }else{
                $scope.shadow.fadeOut(300);
                alternateShadow = false;
            }
        },

        slickNav: function(btNavCurrent){
            btNavCurrent.toggleClass('clicked');
            $scope.nav.this.toggleClass('open');
        },

        events: function(){
            // Event of Slick menu in the responsive version
            $scope.nav.btNav.click(function(event) {
                event.preventDefault();
                dashboard.shadow();
                dashboard.slickNav($(this));
            });

            $scope.shadow.click(function(event) {
                event.preventDefault();
                $scope.shadow.fadeOut(300);
                $scope.nav.this.removeClass('open');
                $scope.nav.btNav.removeClass('clicked');
                $scope.boxOptions.this.removeClass('show-box');
                alternateShadow = false;
            });

            $(window).load(function() {
                dashboard.changeSituation.changeFlags();
            });
        },

        init: function() {
            dashboard.events();
            dashboard.boxOptions.init();
            dashboard.changeSituation.init();

            // Check if the current resolution is equal to 768px.
            if (isMobile.any768()){
                dashboard.mobile();

                $(window).load(function() {
                    dashboard.tabsDashboard.getDimensionsTabs($scope.tabs.tabQuestions.content, 0);
                });
            }
        }
    }

    dashboard.tabsDashboard = {
        // Methods
        // ---------

        // Method that captures the tab height that is active
        getDimensionsTabs: function($tabCurrent, desconto) {
            var currentInnerHeight = $tabCurrent.innerHeight();
            $scope.contents.home.innerHeight(currentInnerHeight + desconto);
        },

        events: function(){
            $scope.tabs.btAlternador.click(function(event) {
                event.preventDefault();
                /*
                    The transition between tabs in the mobile version is powered from the tap in
                    btAlternador element, it is checked whether the event was fired earlier, if so, the
                    tabQuestion is displayed, otherwise the tabProfessional will be displayed.
                */

                // Hides all visivels tabs, for passing only be shown the tab clicked
                $scope.contents.home.find('section').removeClass('show');

                // Checks if the event has been triggered.
                if (!alternateTab) {
                    // The Professionals tab is displayed.
                    $scope.tabs.tabProfessionals.this.addClass('show');

                    // Assigns to the current tab a new height
                    dashboard.tabsDashboard.getDimensionsTabs($scope.tabs.tabProfessionals.content, 50);

                    $(this).css('left', '0');

                    // Assigns true to the next tap, is switched to the tabQuestion.
                    alternateTab = true;
                }else{
                    // The Questions tab is displayed.
                    $scope.tabs.tabQuestions.this.addClass('show');

                    // Assigns to the current tab a new height
                    dashboard.tabsDashboard.getDimensionsTabs($scope.tabs.tabQuestions.content, 0);

                    $(this).css('left', 'auto');

                    // Assigns true to the next tap, is switched to the tabProfessional.
                    alternateTab = false;
                }
            });
        },

        init: function() {
            this.events();
        }
    }

    dashboard.search = {

        // Methods
        // ---------

        showSearch: function(){
            $scope.logo.fadeOut(200);

            setTimeout(function() {
                $scope.search.input.fadeIn();
                $scope.search.input.focus();
                $scope.search.btBack.fadeIn();
                $scope.header.addClass('show-search');
            }, 250);
        },

        hideSearch: function(){
            $scope.search.input.fadeOut();
            $scope.search.btBack.fadeOut();
            $scope.search.input.val('');

            setTimeout(function(){
                $scope.header.removeClass('show-search');
                $scope.logo.fadeIn(200);
                $scope.html.removeClass('fixed');
                $scope.html.removeClass('show-topics');
            }, 250);
        },

        events: function(){
            $scope.search.btSearch.click(function(event) {
                event.preventDefault();
                dashboard.search.showSearch();
            });

            $scope.search.btBack.click(function(event) {
                event.preventDefault();
                dashboard.search.hideSearch();
            });
        },

        init: function(){
            dashboard.search.events();
        }
    }

    dashboard.boxOptions = {
        // Methods
        // ---------

        showBox: function(currentBox){
            $('.content').find('*').removeClass('show-box');

            if (test === 0) {
                currentBox.parent().addClass('show-box');
                test = 1
            }else{
                if (!currentBox.parent().hasClass('show-box')) {
                    currentBox.parent().addClass('show-box');
                }

                currentBox.parent().removeClass('show-box');
                test = 0
            }
        },

        hideBox: function(){
            dashboard.shadow();
            $scope.boxOptions.this.removeClass('show-box');
        },

        events: function(){
            $scope.boxOptions.btOptions.click(function(event) {
                event.preventDefault();
                dashboard.boxOptions.showBox($(this));
            });

            $scope.btMyAccount.click(function(event) {
                event.preventDefault();
                dashboard.boxOptions.showBox($(this));
            });

            $scope.boxOptions.btCancel.click(function(event) {
                event.preventDefault();
                dashboard.boxOptions.hideBox();
            });
        },

        init: function(){
            dashboard.boxOptions.events();
        }
    }

    dashboard.changeSituation = {
        // Methods
        // ---------

        changeFlags: function(){
            from = $('.from .selected').find('.flag').attr('class');
            to = $('.to .selected').find('.flag').attr('class');

            if ( from && to ){

                from = from.split(' ')[1];
                to = to.split(' ')[1];

                textFrom = $('.from .selected').find('.ddlabel').text();
                textTo = $('.to .selected').find('.ddlabel').text();

                $scope.changeSituation.flag.from.addClass(from);
                $scope.changeSituation.flag.to.addClass(to);
                $scope.changeSituation.country.from.text(textFrom);
                $scope.changeSituation.country.to.text(textTo);
            }
        },

        events: function(){
            $scope.changeSituation.btChangeSituation.click(function(event) {
                event.preventDefault();
                $scope.situations.situation.fadeOut();
                $scope.situations.changeSituation.fadeIn();

                setTimeout(function() {
                    $scope.changeSituation.flag.from.removeClass(from);
                    $scope.changeSituation.flag.to.removeClass(to);
                }, 300);
            });
        },

        init: function(){
            dashboard.changeSituation.events();
        }
    }

    dashboard.init();
});
