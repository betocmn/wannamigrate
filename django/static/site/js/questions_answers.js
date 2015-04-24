function onToggleFollow( evt )
{
    evt.preventDefault();

    elm = $( this );
    // Gets the active url on the link.
    var active_url = elm.attr( "href" );
    // Gets the active name of the link.
    var active_name = elm.attr( "data-name" );
    // Gets the toggle url of the link.
    var toggle_url = elm.attr( "data-toggle-url" );
    // Gets the toggle name of the link.
    var toggle_name = elm.attr( "data-toggle-name" );

    // Request the active URL
    $.get( active_url, { "_": $.now() }, function( data ){
        // Updates the name of the button
        counter = elm.find( "span.count" ).clone();
        elm.html('').append( toggle_name ).append( " " ).append( counter );

        // Updates the counter
        counter.text( data );

        // Switches the active name and URL with the toggle values.
        // toggle -> active
        elm.attr( "data-name", toggle_name );
        elm.attr( "href", toggle_url );
        // active -> toggle
        elm.attr( "data-toggle-url", active_url );
        elm.attr( "data-toggle-name", active_name );

    }).fail(function(httpObj, text){
        if ( httpObj.status == 401 )
            window.location.href = evt.data.redirect_url;
    });
}

function onUpvoteClicked( evt )
{
    evt.preventDefault();

    elm = $( this );
    // Gets the active url on the link.
    var active_url = elm.attr( "href" );
    // Gets the targets selectors to update the counter.
    var target_selectors = elm.attr( "data-upvote-counter-selector" );

    // Request the active URL
    $.get( active_url, { "_": $.now() }, function( data ){
        // Updates the counter
        $( target_selectors ).text( data );

    }).fail(function(httpObj, text){
        if ( httpObj.status == 401 )
            window.location.href = evt.data.redirect_url;
    });
}