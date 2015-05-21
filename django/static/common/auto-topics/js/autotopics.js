(function ( $ ) {
    $.fn.autotopics = function( options )
    {
        // Default configurations, do not use this inside the plugin.
        // You should use the settings var that extends this default settings with the
        // options passed by the user.
        var defaults = 
        {
            opts : [],  // the topics options for the autocomplete.
            element_name : this.attr( "name" ),
            element_id : this.attr( "id" ),
            element_placeholder : this.attr( "placeholder" ),
            target : ".topics-container",
            wrapper : "span",
            wrapper_class : "topic",
        };

        var selected_topics = [];

        // Settings
        var settings = $.extend( defaults, options );


        
        // Hides the element
        this.hide();
        
        // Fill the plugin options with the selectbox options.
        this.find( "option" ).each( function( index, element ){ 
            settings.opts.push( { label : element.text, value : element.value  } );
        });

        // Creates the search input for the topics
        var search_input = $( "<input/>" ).attr( "placeholder", settings.element_placeholder ).attr( "id", "topics-input" ).insertAfter( this );

        // Creates the container
        var topics_container = $( "<div/>" ).attr( "class", "topics-container" ).insertAfter( search_input );


        // Registers the autocomplete for the topics search input
        search_input.autocomplete({
            source: settings.opts,
            select: on_add_topic,
            change: update_input_GUI,
            focus: update_input_GUI,
        });

        // Adds all the selected options to the topics container
        this.find( "option:selected" ).each( function( index, element ) {
            // Adds the selected option to the hidden inputs list
            add_topic_UI( element.label, element.value );
        });

        // Removes the selectbox
        this.remove();


         /** Removes the topic from the selected topics list.
            @param topic_id The id of the topic to be removed. */
        function on_remove_topic( topic_id )
        {
            selected_topics.splice( selected_topics.indexOf( topic_id ), 1 );
            remove_topic_UI( topic_id );
        }

        function remove_topic_UI( topic_id )
        {
            $( "#topic-id-" + topic_id ).remove();
            $( "#topics-input" ).val( "" );
        }

        /** Adds a topic to the selected topics list.
            @param event The event data.
            @param ui The ui element data. */
        function on_add_topic( event, ui )
        {
            if ( selected_topics.indexOf( ui.item.value ) == -1 )
            {
                selected_topics.push( ui.item.value );
                add_topic_UI( ui.item.label, ui.item.value );
            }

            $( "#topics-input" ).val( "" );

            return false;
        }

        /**
            Adds a topic to the selected topics list.
        **/
        function add_topic_UI( topic_label, topic_id )
        {

            // Creates a span element which contains the graphical information about the topic 
            // and a hidden input containing the topic_id.
            $( settings.target ).append(
                $( "<" + settings.wrapper + "/>" ).attr( "class", settings.wrapper_class ).attr( "id", "topic-id-" + topic_id )
                .append(
                    $( "<a/>" ).attr( "class", "tag-link" ).attr( "href", "#" ).text( topic_label )
                    .click(function( e ){
                        on_remove_topic( topic_id )
                        e.preventDefault();
                    })
                    .hover(function(){
                        $(this).toggleClass( "country" )
                    })
                )
                .append(
                    // Hidden input
                    $( "<input/>" ).attr( "type", "hidden" ).attr( "name", settings.element_name ).attr( "value", topic_id )
                )
            );

            // Clears input data
            $( "#topic-input" ).val( "" );
        }

        /** Updates the GUI of the input of the autocomplete, filling the input with
            the label of the autocomplete item.
            @param event The event data.
            @param ui The ui element data. */
        function update_input_GUI( event, ui ) {
            $( "#topic-input" ).val( ui.item.label );
            return false;
        }
    };
}( jQuery ));

