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
        counter.text( to_kmi( data ) );

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


function onXToggleButtonClicked( evt )
{
    evt.preventDefault();
    elm = $( this );

    // Gets the active name of the link.
    var primary_action_name = elm.attr( "data-primary-action-name" );
    // Gets the toggle name of the link.
    var secondary_action_name= elm.attr( "data-secondary-action-name" );

    // Peform the request...
    $.get( elm.attr( "href" ), { "_": $.now() }, function( data ){

        name_container = elm.find( "span.name" )
        total_container = elm.find( "span.count" )

        current_name = data.primary_action ? primary_action_name : secondary_action_name;
        current_total = parseInt( data.total );

        if ( name_container.length )    // if name container exists
            name_container.text( current_name );
        if ( total_container.length )  // if counter container exists
            total_container.text( to_kmi( current_total ) )

        if ( data.primary_action )
            elm.addClass( "primary-action" );
        else
            elm.removeClass( "primary-action" );

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
        $( target_selectors ).text( to_kmi( data ) );

    }).fail(function(httpObj, text){
        if ( httpObj.status == 401 )
            window.location.href = evt.data.redirect_url;
    });
}

/** Updates the counter of the given selector with value.
    @param selector The selector of the element to update the counter.
    @param value The value to put on the field.
**/
function updateCounter( selector, value )
{
    return $( selector ).html( '(' + to_kmi( value ) + ')' );
}

/** Updates the number of following topics */
function updateFollowingTopicsCounter( value )
{
    return updateCounter( "#following_topics_counter", value );
}

/** Updates the number of following topics */
function updateAnswersCounter( value )
{
    return updateCounter( "#answers_counter", value );
}

/** Updates the number of following posts */
function updateReadingListCounter( value )
{
    return updateCounter( "#reading_list_counter", value );
}

/** Updates the number of following users */
function updateUsersFollowingCounter( value )
{
    return updateCounter( "#users_following_counter", value );
}

/** Updates the number of followers  */
function updateUsersFollowersCounter( value )
{
    return updateCounter( "#users_followers_counter", value );
}

/** Updates the number of following topics */
function updatePostFollowersCounter( value )
{
    return updateCounter( "#post_followers_counter", value );
}



/** Converts a number to it's kmi representation
    @param value The value to be converted
    @return The kmi representation of the value.
**/
function to_kmi( value )
{
    temp = parseInt( value );

    MI = 1000000;
    K = 1000;

    if ( temp >= MI )
    {
        if ( temp % MI == 0 )
            return parseInt( temp / MI ) + " mi";
        else
            return parseFloat( temp / MI ).toFixed( 1 ) + " mi";
    }
    else if ( temp >= K )
    {
        if ( temp % K == 0 )
            return parseInt( temp / K ) + " k";
        else
            return parseFloat( temp / K ).toFixed( 1 ) + " k";
    }
    else
        return temp;
}