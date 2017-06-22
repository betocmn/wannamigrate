
var $attr,
facebook = {

    // Internal attributes to be used on this module
    attributes: {
        facebook_login_url: '',
        redirect_url: '',
        facebook_app_id: '',
        facebook_button_element: '',
        facebook_loading_element: '',
    },

    // Constructor
    setup_login: function(args) {

        // Receives parameters
        $attr = this.attributes;
        $attr.facebook_login_url = args.facebook_login_url;
        $attr.redirect_url = args.redirect_url;
        $attr.facebook_app_id = args.facebook_app_id;
        $attr.facebook_button_element = args.facebook_button_element;
        $attr.facebook_loading_element = args.facebook_loading_element;

        // Sets up facebook login
        $.ajaxSetup({ cache: true });
        $.getScript('//connect.facebook.net/en_US/sdk.js', function(){

            // Sets up facebook loading
            var $facebook_button = $($attr.facebook_button_element);
            var $facebook_loading = $($attr.facebook_loading_element);

            // Starts up Facebook JS SDK
            FB.init({
                appId: $attr.facebook_app_id,
                cookie: true,
                version: 'v2.9' // or v2.0, v2.1, v2.2, v2.3
            });

            // Ajax request to login facebook user on django
            var process_facebook_user = function(login_response) {
                var params = {
                    facebook_user_id: login_response.authResponse.userID,
                    facebook_access_token: login_response.authResponse.accessToken
                };
                $.post($attr.facebook_login_url, params, function (data) {
                    if(data.status == 'success'){
                        window.location = $attr.redirect_url;
                    } else {
                        $facebook_loading.hide();
                        $facebook_button.show();
                    }
                });
            }


            // Sets up Facebook Login actions
            $facebook_button.click(function () {
                $facebook_button.hide();
                $facebook_loading.show();
                FB.login(function(response){
                    if (response.status === 'connected') {
                        process_facebook_user(response);
                    } else {
                        $facebook_loading.hide();
                        $facebook_button.show();
                    }
                }, {scope: 'public_profile,email,user_birthday'});
            });

        });


    },

};
