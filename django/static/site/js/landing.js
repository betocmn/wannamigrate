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

$(window).load(function() {
    imagesResize({
        element: '.img',
        width: 1920,
        height: 1080
    });
});

$(window).resize(function(){
    imagesResize({
        element: '.img',
        width: 1920,
        height: 1080
    });
});