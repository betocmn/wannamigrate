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

// bg
var cropImage = 0;
var timeoutId = null;
var index = null;

// new height
var newHeight = 0;
var newWidth = 0;

function imagesResize(options){
    resizing = true;

    // window.resize delay
    clearTimeout( timeoutId );
    timeoutId = setTimeout(function() {
        resizing = false;
        index = null;
    }, 400);

    var iWidth = options.width;
    var iHeight = options.height;

    var wWidth = window.innerWidth;
    var wHeight = window.innerHeight;

    var arBrowser = wWidth/wHeight;
    var arImage = iWidth/iHeight;

    var arWidth = iWidth/wWidth;
    var arHeight = iHeight/wHeight;

    if ( arBrowser>1 ) {
        if (arHeight < arWidth) {
            newHeight = wHeight;
            newWidth = (wHeight*arImage);
        } else {
           newHeight = (wWidth/arImage);
           newWidth = wWidth;
        }
    } else {
        if (arHeight < arWidth) {
            newHeight = wHeight;
            newWidth = (wHeight*arImage);
        } else {
           newHeight = (wWidth/arImage);
           newWidth = wWidth;
        }
    }

    cropTop = ( wHeight - newHeight )/2;
    cropLeft = ( wWidth - newWidth )/2;

    $(options.element).css({ height: newHeight, width: newWidth, marginTop: cropTop, marginLeft: cropLeft});
}

var $scope = {
    btAlternador : $('.bt-alternator'),
    contentHome : $('.content.home'),
    logo : $('.logo'),
    header : $('header'),
    btNav : $('.bt-nav'),
    nav : $('nav'),
    navLink : $('.nav-dashboard .nav-link'),
    btLogin : $('.bt-login'),
    html : $('html'),
    dashboard : $('.dashboard'),
    contentDashboard : $('.dashboard .content'),
    shadow : $('.interaction .shadow'),
    contentHire : $('.content.hire'),
    contentHiring : $('.content.hiring'),

    situation : {
        flag : {
            from: $('.situation .from .flag'),
            to: $('.situation .to .flag')
        },

        country : {
            from : $('.situation .from .country'),
            to : $('.situation .to .country'),
        }
    },

    interactions : {
        this : $('.hiring .interactions'),
        interactionLink : $('.hiring .interaction-link'),
        interaction : $('.hiring .interaction')
    },

    boxOptions : {
        this : $('.box-options '),
        btCancel :  $('.bt-cancel'),
        btOptions :  $('.bt-options'),
        shadow :  $('.box-options .shadow')
    },

    contentSearch : {
        btSearch : $('.search .bt-search'),
        input : $('.search input'),
        btBack : $('.search .bt-back')
    },

    sectionProfessionals : {
        this : $('.home .professionals'),
        professional : $('.professional'),
        content : $('.content-professionals')
    },

    sectionQuestions : {
        this : $('.home .questions'),
        content : $('.content-questions')
    }
}

function ajusteAlturaAlternador(section, desconto) {
    var $sectionCurrent = {
        current : $(section)
    }

    currentInnerHeight = $sectionCurrent.current.innerHeight();
    $scope.contentHome.innerHeight(currentInnerHeight + desconto);
}

function transitionSections(nextSection) {
    $scope.contentDashboard.each(function(index, el) {
        if ($(el).hasClass(nextSection)) {
            $(this).fadeIn();
        }else{
            $(this).fadeOut();
        }
    });
}

var from,
    to;
    
function addFlagSituations() {

    from = $('.from.field ul .selected').find('.flag').attr('class');
    to = $('.to.field ul .selected').find('.flag').attr('class');

    if ( from && to ){

        from = from.split(' ')[1];
        to = to.split(' ')[1];

        textFrom = $('.from.field ul .selected').find('.ddlabel').text();
        textTo = $('.to.field ul .selected').find('.ddlabel').text();

        $scope.situation.flag.from.addClass(from);
        $scope.situation.flag.to.addClass(to);
        $scope.situation.country.from.text(textFrom);
        $scope.situation.country.to.text(textTo);

    }

}

if (isMobile.any768()) {
    var currentInnerHeight,
        testAlternador = false

    $scope.contentSearch.btSearch.click(function(event) {
        event.preventDefault();
        $scope.logo.fadeOut(200);

        setTimeout(function() {
            $scope.contentSearch.input.fadeIn();
            $scope.contentSearch.input.focus();
            $scope.contentSearch.btBack.fadeIn();
            $scope.header.addClass('show-search');
        }, 250);
    });

    $scope.contentSearch.btBack.click(function(event) {
        event.preventDefault();
        $scope.contentSearch.input.fadeOut();
        $scope.contentSearch.btBack.fadeOut();
        $scope.contentSearch.input.val('');

        setTimeout(function(){
            $scope.header.removeClass('show-search');
            $scope.logo.fadeIn(200);
            $scope.html.removeClass('fixed');
            $scope.html.removeClass('show-topics');
        }, 250);
    });

    $scope.boxOptions.shadow.click(function(event) {
        event.preventDefault();
        $scope.boxOptions.this.removeClass('show-box');
    });
}

$(window).load(function() {
    imagesResize({
        element: '.img',
        width: 1920,
        height: 1080
    });

    addFlagSituations();

    ajusteAlturaAlternador($scope.sectionQuestions.content, 0);
});

$(window).resize(function(){
    imagesResize({
        element: '.img',
        width: 1920,
        height: 1080
    });

    if (!testAlternador) {
        ajusteAlturaAlternador($scope.sectionQuestions.content, 0);
    }else{
        ajusteAlturaAlternador($scope.sectionProfessionals.content, 50);
    }
});

$scope.btAlternador.click(function(event) {
    event.preventDefault();
    $scope.contentHome.find('section').removeClass('show');
    if (!testAlternador) {
        $scope.sectionProfessionals.this.addClass('show');
        ajusteAlturaAlternador($scope.sectionProfessionals.content, 50);

        $(this).css('left', '0');
        testAlternador = true;
    }else{
        $scope.sectionQuestions.this.addClass('show');
        ajusteAlturaAlternador($scope.sectionQuestions.content, 0);

        $(this).css('left', 'auto');
        testAlternador = false;
    }
});

// nav Mobile
var testNavOpen = false;

$scope.btNav.click(function(event) {
    $(this).toggleClass('clicked');

    if (!testNavOpen) {
        $scope.nav.addClass('open');
        $scope.shadow.fadeIn();
        $scope.nav.height(175);
        $scope.html.addClass('fixed');
        testNavOpen = true;
    }else{
        $scope.nav.height(0);
        $scope.html.removeClass('fixed');
        $scope.shadow.fadeOut(300);
        setTimeout(function() {
            $scope.nav.removeClass('open');
        }, 300);
        testNavOpen = false;
    }

    $scope.btLogin.removeClass('button');
});

$scope.shadow.click(function(event) {
    $scope.btNav.trigger('click');
});

$('.bt-change').click(function(event) {
    event.preventDefault();
    addFlagSituations();
});

$('.bt-change-situation').click(function(event) {
    event.preventDefault();

    setTimeout(function() {
        $('.situation .from .flag').removeClass(from);
        $('.situation .to .flag').removeClass(to);     
    }, 300);
});

$scope.logo.click(function(event) {
    event.preventDefault();
    transitionSections('home');
});

$scope.navLink.click(function(event) {
    event.preventDefault();
    var currentSection = $(this).attr('data-link');
    if (currentSection === 'professionals') {
        transitionSections('hire');
    };
});

$scope.sectionProfessionals.professional.click(function(event) {
    event.preventDefault();
    transitionSections('hiring');
});

$scope.interactions.interactionLink.click(function(event) {
    event.preventDefault();
    // $scope.interactions.in.addClass('active');
    $scope.interactions.interactionLink.removeClass('active');
    $(this).addClass('active');

    var interactionName = $(this).attr('class').split(' ')[1];
    var currentInteraction = "." + interactionName.replace('bt-', '');

    $scope.interactions.interaction.fadeOut();
    $scope.interactions.this.find(currentInteraction).fadeIn();
});

// Situation
$('.bt-change').click(function(event) {
    event.preventDefault();
    $('.change-situation').fadeOut();
    $('.situation').fadeIn();
});

$('.bt-change-situation').click(function(event) {
    event.preventDefault();
    $('.situation').fadeOut();
    $('.change-situation').fadeIn();
});

//Options (Share, Report, Cancel)
$scope.boxOptions.btOptions.click(function(event) {
    event.preventDefault();
    var currentBox = $(this).closest('div');
    currentBox.find('.box-options').toggleClass('show-box');
});

$scope.boxOptions.btCancel.click(function(event) {
    event.preventDefault();
    $scope.boxOptions.this.removeClass('show-box');
});
