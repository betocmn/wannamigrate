/**
 * Resizes the iframe to fit its height on the screen.
 * @param obj The iframe to resize.
 * */
function resizeIframe( obj )
{
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
}