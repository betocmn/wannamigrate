 /** A pseudo-enum to store SceneController's state */
SceneControllerState = 
{
  IDLE : 0,
  ON_SCENE_ENTER: 1,
  LOADING_NEXT_PAGE: 2,
  LOADING_PREV_PAGE: 3,
}

SceneController = 
{
  /////////////////////////////
  // CONSTANTS
  /////////////////////////////
  INNER_ELEMENTS_TRANSITION_TIME : 400,

  
  /////////////////////////////
  // VARIABLES
  /////////////////////////////
  /** The state of the Scene Controller. */
  state : SceneControllerState.IDLE,
  /** Base URL of the page. */
  base_url: "",
  /** The browser can do CSS Transitions? */
  browser_support : false,
  /** The current page being displayed */
  curr_page : 0,
  /** The total number of pages */
  n_pages : 0,
  /** Left divs */
  left : [],
  /** Right divs */
  right : [],
  /** The feature counter used by onFeatureEnds */  
  feature_counter : 0,
  /** The total number of features */
  n_features : 6,

  
  ///////////////////////////////
  // METHODS
  ///////////////////////////////
  /** Loads the next page if its possible. */
  nextPage : function()
  {
    if ( SceneController.curr_page >= ( SceneController.n_pages - 1 ) )
      return;

    SceneController.state = SceneControllerState.LOADING_NEXT_PAGE;
    InputHandler.lock();
    SceneController.onSceneLeave();
  },
  
  /** Loads the previous page if its possible. */
  prevPage : function()
  {
    if ( SceneController.curr_page <= 0 )
      return;

    SceneController.state = SceneControllerState.LOADING_PREV_PAGE;
    InputHandler.lock();
    SceneController.onSceneLeave();
  },

  /** Handles the animation on the features off page 3. At the end it calls the
  onSceneLeave function if the user is leaving the page or just unlocks the input
  if it was entering on the page. */
  onFeatureEnds : function()
  {
    console.log( "on feature ends..." );
    // Always unbind transitionend on the previous feature.
    if ( SceneController.feature_counter > 0 )
      $( ".feature" ).eq( SceneController.feature_counter - 1 ).unbind( "transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd" );

    // Checks if all animations ended.
    if ( SceneController.feature_counter >= SceneController.n_features )
    {
      // Resets the feature counter
      SceneController.feature_counter = 0;

      // Scene enter ended, just sets the SceneController's state to Idle and unlocks the input.
      if ( SceneController.state == SceneControllerState.ON_SCENE_ENTER )
      {
        SceneController.state = SceneControllerState.IDLE;
        InputHandler.unlock();
        return;
      }
      else  // Scene leave ended...
        return SceneController.onSceneLeaveEnds();
    }

    // Gets the current feature.
    curr_feature = $( ".feature" ).eq( SceneController.feature_counter );   
    
    // Binds transitionend event to the feature.
    curr_feature.bind( "transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd", SceneController.onFeatureEnds );

    // Hide/Unhides the feature according to the SceneController's state.
    if ( SceneController.state == SceneControllerState.ON_SCENE_ENTER )
      curr_feature.removeClass( "hide" );
    else
      curr_feature.addClass( "hide" );
    
    // Increment the feature counter.
    SceneController.feature_counter++;

  },

  /** Called when the page is leaving, handles the required animations of leaving elements 
  before changing the page's background. */
  onSceneLeave : function()
  {
    console.log( "scene leave: " + SceneController.curr_page );
    switch ( SceneController.curr_page )
    {
      case 0:
        // disables the page elements
        $( "#bt-more" ).hide();
        $("#page0-content").fadeOut( SceneController.INNER_ELEMENTS_TRANSITION_TIME, SceneController.onSceneLeaveEnds );
        break;
      case 1:
        $( "#bt-more" ).hide();
        $( "#l1h" ).addClass( "hide" );
        $( "#r1ul" ).addClass( "hide" );
        $( "#r1-signup" ).fadeOut( SceneController.INNER_ELEMENTS_TRANSITION_TIME, SceneController.onSceneLeaveEnds );
        break;
      case 2:
        //SceneController.onFeatureEnds();
        $( ".feature" ).hide().addClass( "hide" );
        SceneController.onSceneLeaveEnds();
        $(".feature").show();
        break;
      case 3:
        $( "#bt-more" ).hide();
        $("#r3-signup").fadeOut( SceneController.INNER_ELEMENTS_TRANSITION_TIME, SceneController.onSceneLeaveEnds );
        break;
      case 4:
        SceneController.onSceneLeaveEnds();
        break;
      default:
        break;
    }
  },

  /** Called when the Scene Leave function ends. This function handles the bg transition process. */ 
  onSceneLeaveEnds : function()
  {
    console.log( "changing page... ");
    // Am I loading the next page?
    if ( SceneController.state == SceneControllerState.LOADING_NEXT_PAGE )
    {
      SceneController.curr_page++;

      SceneController.left[ SceneController.curr_page - 1 ].removeClass( "active" ).addClass( "prev" );
      SceneController.left[ SceneController.curr_page ].removeClass( "next" ).addClass( "active" );
      if ( SceneController.curr_page < SceneController.n_pages - 1 )
        SceneController.left[ SceneController.curr_page + 1 ].addClass( "next" );

      SceneController.right[ SceneController.curr_page - 1 ].removeClass( "active" ).addClass( "prev" );
      SceneController.right[ SceneController.curr_page ].removeClass( "next" ).addClass( "active" );
      if ( SceneController.curr_page < SceneController.n_pages - 1 )
        SceneController.right[ SceneController.curr_page + 1 ].addClass( "next" );
    }
    else
    {
      SceneController.curr_page--;

      SceneController.left[ SceneController.curr_page + 1 ].removeClass( "active" ).addClass( "next" );
      SceneController.left[ SceneController.curr_page ].removeClass( "prev" ).addClass( "active" );
      if ( SceneController.curr_page > 1 )
        SceneController.left[ SceneController.curr_page - 1 ].addClass( "prev" );

      SceneController.right[ SceneController.curr_page + 1 ].removeClass( "active" ).addClass( "next" );
      SceneController.right[ SceneController.curr_page ].removeClass( "prev" ).addClass( "active" );
      if ( SceneController.curr_page > 1 )
        SceneController.right[ SceneController.curr_page - 1 ].addClass( "prev" );
    }


  },
  
  /** Called when the page is entering, handles the required animations of entering elements 
  after changing the page's background. */
  onSceneEnter : function( e )
  {

    // Make sure that only background divs will process the bind event
    // (Without this code the transitionend on .feature elements will be catched too).
    if( e.target != this ) return; 

    // Changes the scene controller's state.
    SceneController.state = SceneControllerState.ON_SCENE_ENTER;

    console.log( "scene enter: " + SceneController.curr_page );
    SceneController.appendURL();
    switch ( SceneController.curr_page )
    {
      case 0:
        $( "#menu" ).removeClass( "translucid" );
        $( "#bt-more" ).attr( "class", "gui" ).show();
        $("#page0-content").fadeIn( SceneController.INNER_ELEMENTS_TRANSITION_TIME );
        InputHandler.unlock();
        break;
      case 1:
        $( "#menu" ).addClass( "translucid" );
        $( "#bt-more" ).attr( "class", "gui page1" ).show();
        $( "#l1h" ).removeClass( "hide" );
        $( "#r1ul" ).removeClass( "hide" );
        $("#r1-signup").fadeIn( SceneController.INNER_ELEMENTS_TRANSITION_TIME );
        InputHandler.unlock();
        break;
      case 2:
        // Obs: The onFeatureEnds function will unlock the input.
        SceneController.onFeatureEnds();
        break;
      case 3:
        $( "#bt-more" ).attr( "class", "gui page3" ).show();
        $("#r3-signup").fadeIn( SceneController.INNER_ELEMENTS_TRANSITION_TIME );
        InputHandler.unlock();
        break;
      case 4:
        InputHandler.unlock();
        break;
      default:
        break;
    }

    

  },

  /** Appends the number of the current page at the end of the URL. */
  appendURL : function() 
  {
    window.location.href = SceneController.base_url + "#" + SceneController.curr_page;
  },

  /** Initializes the SceneController's elements. */
  init : function()
  {
    // This URL will be used to append the active page that user is looking.
    // TODO: Replace window.location.href with the index URL in django.
    SceneController.base_url = window.location.href;   
    
    // Initializes the total number of pages
    SceneController.n_pages = $( "#right > .section-item" ).size();
    
    // Initializes the total number of features
    SceneController.n_features = $( ".feature" ).size();
    
    // Initializes vectors
    for ( var i = 0; i < SceneController.n_pages; i++ )
    {
      SceneController.left.push( $( ("#l" + i ) ) );
      SceneController.right.push( $( ("#r" + i ) ) );

      // Binds trasitionend event handler only for sections 0, 2 and 4. This way 
      // only one call on "onSceneEnter" will occur. If we bind transitionend for all
      // backgrounds transitions, then when the user change the page between 0 and 1
      // two calls to "onSceneEnter" will occur, the leaving of background 0 and the entering
      // of background 1.
      if ( i % 2 == 0 )
        SceneController.right[i].bind( "transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd", SceneController.onSceneEnter );
    }

    // Hides page elements that will appear with animation.
    $( "#r1-signup" ).hide();
    $( "#r3-signup" ).hide();

    // Register input handlers
    $( document ).mousewheel( InputHandler.onMouseWheel );
    $( document ).keydown( InputHandler.onKeyDown );

    // Bounce the more button at the beginning.
    $("#bt-more").effect( "bounce", 2000 );
    
  },
};


/** A structure that handles all kind of inputs. */
InputHandler = 
{
  /** Flag indicating that the input is locked and should be ignored. */
  is_locked : false,
  /** Flag indicating that the mouse is locked and should be ignored. */
  mouse_lock : false,

  /** Locks the input handler */
  lock : function()
  {
    console.log( "Locking InputHandler..." ); 
    InputHandler.is_locked = true; 
  },
  /** Unlocks the input handler */
  unlock : function()
  { 
    console.log( "Unlocking InputHandler..." );
    InputHandler.is_locked = false;
  },

  /** Checks if the keys UP and DOWN was pressed and calls the corresponding
  function on SceneController. */
  onKeyDown : function( e )
  {
    console.log( "InputHandler event: KeyDown " );
    console.log( "InputHandler is locked: " + InputHandler.is_locked );
    // If the input is locked, nothing to do.
    if ( InputHandler.is_locked )
      return;

    switch(e.which)
    {
        case 38: // up
          console.log( "UP pressed" );
          SceneController.prevPage();
        break;
        case 40: // down
          console.log( "DOWN pressed" );
          SceneController.nextPage();
        break;
        default: return; // exit this handler for other keys
    }
    e.preventDefault(); // prevent the default action (scroll / move caret)
  },

  /** Checks if the mouse was scrolled UP and DOWN and calls the corresponding
  function on SceneController. */
  onMouseWheel : function( e )
  {
    if ( InputHandler.mouse_lock )
      return;
    
    InputHandler.mouse_lock = true;
    setTimeout( function(){ InputHandler.mouse_lock = false; }, 2000 );

    console.log( "InputHandler event: MouseWheel " );
    console.log( "InputHandler is locked: " + InputHandler.is_locked );

    // If the input is locked, nothing to do.
    if ( InputHandler.is_locked )
      return;

    if ( e.deltaY < 0 )
    {
      console.log( "ScrollDOWN" );
      SceneController.nextPage();
    }
    else
    {
      console.log( "ScrollUP" );
      SceneController.prevPage();
    }
  },
};

