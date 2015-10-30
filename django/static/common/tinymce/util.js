function init_editor( selector, body_class, content_css )
{
    tinymce.PluginManager.add('customh1', function(editor, url) {
        // Add a button that opens a window
        editor.addButton('customh1', {
            text: "H",
            title: "Header",
            icon: false,
            onclick:  function() { editor.execCommand( 'mceToggleFormat', false, "h1" ); }
        });
    });


    tinymce.init({
        selector: selector,
        plugins: [
            "autolink lists link image charmap anchor hr customh1",
        ],
        menubar: false,
        statusbar: false,
        toolbar: [ "customh1 bold italic underline strikethrough blockquote | justifyleft justifycenter justifyright justifyfull | bullist numlist | hr link image" ],
        body_class: body_class,
        content_css: content_css,
    });
}