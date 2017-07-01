/**
 * util.js
 * Common javascript functions
 *
 * @author Humberto Moreira <humberto.mn@gmail.com>
 * @version 2.0
 */


/**
 *  Track an event using a 3rd party library
 *
 *  Currently using Drip.co
 *
 */
function track_event(event, data) {
    if(IS_PROD){
        _dcq.push(["track", event, data]);
        if(event == 'placed_order'){
            fbq('track', 'Purchase', data);
        }else if(event == 'completed_quiz'){
            fbq('track', 'Lead');
        }
    }
}


/**
 *  Clears tracking user using a 3rd party library
 *
 *  Currently using Drip.co
 *
 */
function track_logout() {
    return false;
}

/**
 * Get cookie by its name
 *
 */
function get_cookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


/**
 * Checks http method for additional csrf protection
 *
 */
function csrf_safe_method(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


/**
 * Init datatable plugin
 *
 */
function init_datatable($elem, sorting, columns, url) {

        // Init plugin
        var table = $elem.dataTable({
            "bProcessing": true,
            "bServerSide": true,
            "aaSorting": sorting,
            "aoColumns": columns,
            "sAjaxSource": url
        });

        // Modifies some data in the table after its loaded
        $elem.on('draw.dt', function () {

            // Changes color of rows marked as disabled / inactive
            $(".listing-row-disabled").parent().parent().addClass('disabled');

            // Make <tr> clickable to go to the "View" page
            /*
            $(".dataTable tr").click(function(e) {
                if($(e.target).is('button') || $(e.target).is('i') || $(e.target).hasClass('delete_link')){
                    e.preventDefault();
                    return;
                }
                var $link = $(this).find(".listing-view-details");
                if($link.length)
                    window.location = $link.attr('href');
            });
            */
        });

}

/**
 *  Confirm BOX before removing something
 *
 */
function confirm_delete(path ){
    if(confirm('Are you sure you want to delete this item?')) {
        window.location = path;
        return true;
    }
    return false;
}


/**
 *  Highlight fieds that did not pass on PHP Validation
 *
 */
function hightlight_error_element(field_id ){

    $("#" + field_id ).parent().addClass('has-error' );
    /*if ($("#select-" + field_id ).length > 0 ){
        $("#select-" + field_id ).addClass('has-error' );
    }*/

}


/**
*  Remove error highlight from element
*
*/
function remove_hightlight_error_element(field_id, parent_nodes ){

    $("#" + field_id ).parent().removeClass('has-error' );
    /*if ($("#select-" + field_id ).length > 0 ){
        $("#select-" + field_id ).removeClass('has-error' );
    }*/
}


/**
*  Add field to the required list
*
*/
function add_required_field(field, list ){

    // convert to array
    var list = list.split(',' );

    // check if field is already there
    if (!in_array(field, list)){
        list.push(field );
    }

    // convert back to csv string and return it
    return list.join(',' );
} 


/**
*  Remove field from the required list
*
*/
function remove_required_field(field, list ){

    // convert to array
    var list = list.split(',' );

    // loop through array to manually remove item
    for (key in list){
        if (list[key] == field){
            list.splice(key, 1 );
        }
    }

    // convert back to csv string and return it
    return list.join(',' );

} 


/**
 *  Look for required fields that were not set.
 *
 */
function validate_empty_fields(form, required, alert_message ){

    // initial settings
    var error = false;

    // if we have a form and list of required fields
    if (form && required ){

        // set variables
        var elem = form.elements;
        var form_size = form.elements.length;
        var required = required.split(',' );

        // if we don't have a cutom error message
        if (!alert_message ){
            alert_message = "Fill in all required fields!";
        }

        // loop through all form elements
        for (i = 0; i < form_size; i++ ){

            // if id is set and element is in the required array
            if (elem[i].id && in_array(elem[i].id, required)){

                // make sure it is a readable form element
                var text_types = new Array('text', 'password', 'select-one', 'textarea', 'email', 'url', 'number' );
                if (in_array(elem[i].type, text_types)){

                    // validate field
                    if (elem[i].value == ""){	// if it's empty we need to hightlight element as error

                        error = true;
                        hightlight_error_element(elem[i].id );

                    } else { // if it's not empty we put original style

                        remove_hightlight_error_element(elem[i].id );

                    }
                }
            }
        }
    }

    if (error ){
        display_error(alert_message)
        return false;
    } else {
        return true;
    }
}

/**
 *  Check if number is integer or not
 *
 */
function is_integer(value) {
    return /^\d+$/.test(value);
}

/**
 *  Add global notification
 *
 */
function display_notification(type, title, msg) {
    if(typeof PNotify !== 'undefined') {
        new PNotify({
            title: title,
            text: msg,
            icon: false, // 'fa fa-warning'
            delay: 5000,
            opacity: 1,
            type: type, // "notice", "info", "success", or "error".
            buttons: {
                sticker: false
            }
        });
    }
}


/**
 *  Add global error message
 *
 */
function display_error(msg) {
    $("#global_alert_error_msg").html(msg);
    $("#global_alert_error").show();
    display_notification('error', 'Error', msg);
    window.scrollTo(0, 0);
}

/**
 *  Add global success message
 *
 */
function display_success(msg) {
    $("#global_alert_success_msg").html(msg);
    $("#global_alert_success").show();
    display_notification('success', 'Success', msg);
    window.scrollTo(0, 0);
}

/**
*  X-Browser isArray(), including Safari
*
*/
function isArray(obj) {
    return obj.constructor == Array;
}


/**
*  Equivalent to PHP's in_array()
*
*/
function in_array (needle, haystack, argStrict) {
    // http://kevin.vanzonneveld.net
    // +   original by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +   improved by: vlado houba
    // *     example 1: in_array('van', ['Kevin', 'van', 'Zonneveld']);
    // *     returns 1: true
    // *     example 2: in_array('vlado', {0: 'Kevin', vlado: 'van', 1: 'Zonneveld'});
    // *     returns 2: false
    // *     example 3: in_array(1, ['1', '2', '3']);
    // *     returns 3: true
    // *     example 3: in_array(1, ['1', '2', '3'], false);
    // *     returns 3: true
    // *     example 4: in_array(1, ['1', '2', '3'], true);
    // *     returns 4: false
 
    var key = '', strict = !!argStrict;
 
    if (strict) {
        for (key in haystack) {
            if (haystack[key] === needle) {
                return true;
            }
        }
    } else {
        for (key in haystack) {
            if (haystack[key] == needle) {
                return true;
            }
        }
    }
 
    return false;
}


/**
*  Equivalent to PHP's number_format()
*
*/
function number_format (number, decimals, dec_point, thousands_sep) {
    // Formats a number with grouped thousands
    //
    // version: 906.1806
    // discuss at: http://phpjs.org/functions/number_format
    // +   original by: Jonas Raoni Soares Silva (http://www.jsfromhell.com)
    // +   improved by: Kevin van Zonneveld (http://kevin.vanzonneveld.net)
    // +     bugfix by: Michael White (http://getsprink.com)
    // +     bugfix by: Benjamin Lupton
    // +     bugfix by: Allan Jensen (http://www.winternet.no)
    // +    revised by: Jonas Raoni Soares Silva (http://www.jsfromhell.com)
    // +     bugfix by: Howard Yeend
    // +    revised by: Luke Smith (http://lucassmith.name)
    // +     bugfix by: Diogo Resende
    // +     bugfix by: Rival
    // +     input by: Kheang Hok Chin (http://www.distantia.ca/)
    // +     improved by: davook
    // +     improved by: Brett Zamir (http://brett-zamir.me)
    // +     input by: Jay Klehr
    // +     improved by: Brett Zamir (http://brett-zamir.me)
    // +     input by: Amir Habibi (http://www.residence-mixte.com/)
    // +     bugfix by: Brett Zamir (http://brett-zamir.me)
    // *     example 1: number_format(1234.56);
    // *     returns 1: '1,235'
    // *     example 2: number_format(1234.56, 2, ',', ' ');
    // *     returns 2: '1 234,56'
    // *     example 3: number_format(1234.5678, 2, '.', '');
    // *     returns 3: '1234.57'
    // *     example 4: number_format(67, 2, ',', '.');
    // *     returns 4: '67,00'
    // *     example 5: number_format(1000);
    // *     returns 5: '1,000'
    // *     example 6: number_format(67.311, 2);
    // *     returns 6: '67.31'
    // *     example 7: number_format(1000.55, 1);
    // *     returns 7: '1,000.6'
    // *     example 8: number_format(67000, 5, ',', '.');
    // *     returns 8: '67.000,00000'
    // *     example 9: number_format(0.9, 0);
    // *     returns 9: '1'
    // *     example 10: number_format('1.20', 2);
    // *     returns 10: '1.20'
    // *     example 11: number_format('1.20', 4);
    // *     returns 11: '1.2000'
    // *     example 12: number_format('1.2000', 3);
    // *     returns 12: '1.200'
    var n = number, prec = decimals;
 
    var toFixedFix = function (n,prec) {
        var k = Math.pow(10,prec);
        return (Math.round(n*k)/k).toString();
    };
 
    n = !isFinite(+n) ? 0 : +n;
    prec = !isFinite(+prec) ? 0 : Math.abs(prec);
    var sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep;
    var dec = (typeof dec_point === 'undefined') ? '.' : dec_point;
 
    var s = (prec > 0) ? toFixedFix(n, prec) : toFixedFix(Math.round(n), prec); //fix for IE parseFloat(0.55).toFixed(0) = 0;
 
    var abs = toFixedFix(Math.abs(n), prec);
    var _, i;
 
    if (abs >= 1000) {
        _ = abs.split(/\D/);
        i = _[0].length % 3 || 3;
 
        _[0] = s.slice(0,i + (n < 0)) +
              _[0].slice(i).replace(/(\d{3})/g, sep+'$1');
        s = _.join(dec);
    } else {
        s = s.replace('.', dec);
    }
 
    var decPos = s.indexOf(dec);
    if (prec >= 1 && decPos !== -1 && (s.length-decPos-1) < prec) {
        s += new Array(prec-(s.length-decPos-1)).join(0)+'0';
    }
    else if (prec >= 1 && decPos === -1) {
        s += dec+new Array(prec).join(0)+'0';
    }
    return s;
}
