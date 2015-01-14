


$( document).ready(function(){

    /* Actions for Landing-Page */
    $( "#login-button" ).click( function() {
        mixpanel.track( "Login Clicked", {
            "from": "Top-Bar"
        });
    });

    $( "#p0-signup" ).click( function() {
        mixpanel.track( "Sign-up Clicked", {
            "from": "Home - Slide 1"
        });
    });

    $( "#r1-signup" ).click( function() {
        mixpanel.track( "Sign-up Clicked", {
            "from": "Home - Slide 2"
        });
    });

    $( "#r3-signup" ).click( function() {
        mixpanel.track( "Sign-up Clicked", {
            "from": "Home - Slide 4"
        });
    });

    $( "#r4-signup" ).click( function() {
        mixpanel.track( "Sign-up Clicked", {
            "from": "Home - Slide 5"
        });
    });


    /* Actions for Login-Page */
    $( "a.signup-switcher" ).click( function() {
        mixpanel.track( "Sign-up Clicked", {
            "from": "Login Page"
        });
    });

    $( "a.login-switcher" ).click( function() {
        mixpanel.track( "Login Clicked", {
            "from": "Signup Page"
        });
    });


    /* Actions for Dashboard */
    $( "a.checkBtn" ).click( function() {
        mixpanel.track( "Check My Situation Clicked", {
            "from": "Dashboard"
        });
    });

    $( "a.applyBtn" ).click( function() {
        mixpanel.track( "Step-by-Step Clicked", {
            "from": "Dashboard"
        });
    });

    $( "a.movingBtn" ).click( function() {
        mixpanel.track( "Hire a Professional Clicked", {
            "from": "Dashboard"
        });
    });

    $( "div.selectAustralia" ).click( function() {
        mixpanel.track( "Australia Clicked", {
            "from": "Dashboard"
        });
    });

    $( "div.selectCanada" ).click( function() {
        mixpanel.track( "Canada Clicked", {
            "from": "Dashboard"
        });
    });

    $( "div.selectNewZealand" ).click( function() {
        mixpanel.track( "New Zealand Clicked", {
            "from": "Dashboard"
        });
    });


});
