(function ( $ ) {
    $.fn.wm_editor = function( options )
    {
        ///////////////////////
        // Configurations
        ///////////////////////

        // Buttons available on this editor
        var editor_buttons = 
        {
            "heading" : 
            {
                title: "Heading",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'formatblock', 'h1' );  },
                classes: "wm-editor-button wm-editor-button-heading",
                fa_icon_classes: "fa fa-header",
            },
            "bold" : 
            {
                title: "Bold",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'bold' );  },
                classes: "wm-editor-button wm-editor-button-bold",
                fa_icon_classes: "fa fa-bold",
            },
            "italic" : 
            {
                title: "Italic",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'italic' );  },
                classes: "wm-editor-button wm-editor-button-italic",
                fa_icon_classes: "fa fa-italic",
            },
            "underline" : 
            {
                title: "Underline",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'underline' );  },
                classes: "wm-editor-button wm-editor-button-underline",
                fa_icon_classes: "fa fa-underline",
            },
            "ol" : 
            {
                title: "Numbered list",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'insertorderedlist' );  },
                classes: "wm-editor-button wm-editor-button-ol",
                fa_icon_classes: "fa fa-list-ol",
            },
            "ul" : 
            {
                title: "Dotted list",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'insertunorderedlist' );  },
                classes: "wm-editor-button wm-editor-button-ul",
                fa_icon_classes: "fa fa-list-ul",
            },
            "quote" : 
            {
                title: "Quote",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'formatblock', 'blockquote' );  },
                classes: "wm-editor-button wm-editor-button-quote",
                fa_icon_classes: "fa fa-quote-left",
            },
            "link" : 
            {
                title: "Link to ...",
                onclick: function( e ) {
                    e.preventDefault(); 
                    var lnk = prompt('Write the URL here','');
                    if( lnk && lnk != '' )
                    {
                        var expression = /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
                        var regex = new RegExp( expression );

                        if ( ! lnk.match( regex ) )
                        {
                            alert( "Invalid URL" );
                            return;
                        }

                        if ( ! lnk.startsWith( "http://" ) && ! lnk.startsWith( "https://" ) )
                            lnk = "http://" + lnk;
                        
                        wm_editor_format( 'createlink', lnk );
                    }
                },
                classes: "wm-editor-button wm-editor-button-link",
                fa_icon_classes: "fa fa-link",
            },
            "remove_format" : 
            {
                title: "Remove formatting",
                onclick: function( e ) { e.preventDefault(); wm_editor_format( 'removeFormat' );  },
                classes: "wm-editor-button wm-editor-button-remove-format",
                fa_icon_classes: "fa fa-ban",
            },

        };

        // Defaults
        var defaults = 
        {
            // List of buttons enabled on the editor
            enabled_buttons : [ "heading", "bold", "italic", "underline", "ol", "ul", "quote", "link" ],

            // Keep the information about the element
            element_name : this.attr( "name" ),
            element_value : this.val(),
            element_id : this.attr( "id" ),
            element_class : this.attr( "class" ),
            element_form : this.closest( "form" )
        };

        // Merge defaults and user defined options into settings.
        var settings = $.extend( defaults, options );


        


        ////////////////////////////
        // INITIALIZATION
        ///////////////////////////

        // Creates the container div
        var editor_container = $( "<div/>" ).attr( "class", "wm-editor-container" );

        // Creates the menu
        var editor_menu = $( "<div/>" ).attr( "class", "wm-editor-menu" );
        for ( var i = 0; i < settings.enabled_buttons.length; i++ )
        {
            // Gets the button's information
            button = editor_buttons[ settings.enabled_buttons[i] ];
            // Creates the icon
            icon = $( "<i/>" ).attr( "class", button.fa_icon_classes );
            // Creates the link wrapper
            bt = $( "<a/>" ).attr( "href", "#" ).attr( "title", button.title ).attr( "class", button.classes ).click( button.onclick );
            bt.append( icon );
            // Appends the button on the menu
            editor_menu.append( bt );
        }

        // Creates the content div
        var editor_content = $( "<div/>" ).attr( "contenteditable", true ).attr( "class", "wm-editor-content" ).addClass( settings.element_class )
                .attr( "id", settings.element_id ).html( settings.element_value );

        // Appends everything on the container
        editor_container.append( editor_menu ).append( editor_content );

        // Inserts the container after the element.
        editor_container.insertAfter( this );

        // Removes the textarea
        this.remove();

        function wm_editor_format( cmd, value ) 
        {
          document.execCommand( cmd, false, value );
          editor_content.focus();
        }

        $( settings.element_form ).submit(function(){
            var content_html = editor_content.html();
            var generated_input = $( "<input/>" ).attr( "type", "hidden" ).attr( "name", settings.element_name ).val( content_html );
            settings.element_form.append( generated_input );
            return true;
        });

    };
}( jQuery ));