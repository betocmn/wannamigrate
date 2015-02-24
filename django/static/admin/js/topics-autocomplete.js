selected_topics = [];

available_topics = [
    {% for topic in topics %}
        { value : {{ topic.id }}, label : "{{ topic.name }}" },
    {% endfor %}
];



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
    $( "#topic-input" ).val( "" );
}

/** Adds a topic to the selected topics list.
    @param event The event data.
    @param ui The ui element data. */
function on_add_topic( event, ui )
{
    if ( selected_topics.indexOf( ui.item.value ) == -1 )
    {
        selected_topics.push( ui.item.value );
        add_topic_UI( ui.item.value, ui.item.label );
    }
    else
        $( "#topic-input" ).val( "" );

    return false;
}

/**
    Adds a topic to the selected topics list.
**/
function add_topic_UI( topic_id, topic_label )
{

    // Creates a span element which contains the graphical information about the topic 
    // and a hidden input containing the topic id.
    var span = $( "<span/>" ).attr( "class", "topic" ).attr( "id", "topic-id-" + topic_id );

    var bt_remove = $( "<i/>" ).attr( "onclick", "on_remove_topic( " + topic_id + " );" )
            .attr( "class", "fa fa-times bt-remove-topic" );
    
    span.append( topic_label ).append( " " ).append( bt_remove );

    $( ".topics-container").append( span );
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



    // JS FORM Validation
    $( "#main_form" ).submit( function() {

        selected_topics_str = selected_topics.join().toString();
        selected_topics_input = $( "<input/>" ).attr( "name", "{{ form.related_topics.name }}" ).val( selected_topics_str );
        $( "#main_form" ).append( selected_topics_input );
        

        return true;

    });



    // Fills the selected topics.
    for ( var i = 0; i < selected_topics.length; i++ )
    {
        var curr_topic_id = selected_topics[ i ];
        var curr_topic_label = "";

        // Searches available_topics to find 
        //the label for the current topic id.
        for ( var j = 0; j < available_topics.length; j++ )
        {
            if ( curr_topic_id == available_topics[ j ].value )
            {
                curr_topic_label = available_topics[ j ].label;
                break;
            }
        }
        // Adds an ui element for the selected topic.
        add_topic_UI( curr_topic_id, curr_topic_label );
    }


    

    // register autocomplete handler to topic-input.
    $( "#topic-input" ).autocomplete({
        source: available_topics,
        select: on_add_topic,
        change: update_input_GUI,
        focus: update_input_GUI,
    });
    