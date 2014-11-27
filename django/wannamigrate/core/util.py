from functools import reduce
from django.db.models import Q
import json
from io import StringIO
from django.core.urlresolvers import reverse
from django.shortcuts import _get_queryset
from calendar import monthrange
from datetime import date, datetime, timedelta
from django.utils.translation import ugettext_lazy as _
from wannamigrate.core.models import UserPersonal
from django.http import HttpResponse
from django.db import models

def calculate_age( birth_date ):
    """
    Calculates age based on birth date

    :param birth_date:
    :return Int:
    """
    if not birth_date:
        return 0

    today = date.today()
    return today.year - birth_date.year - ( ( today.month, today.day) < ( birth_date.month, birth_date.day ) )


def date_difference( start_date, end_date, mode = 'months' ):
    """
    Calculates difference between 2 dates and return in mode (months or years)

    :param start_date:
    :param end_date:
    :param mode:
    :return Mixed:
    """
    months = 0
    while True:
        mdays = monthrange( start_date.year, start_date.month )[1]
        start_date += timedelta( days = mdays )
        if start_date <= end_date:
            months += 1
        else:
            break

    if mode == 'months':
        result = months
    elif mode == 'years':
        result = round( months / 12, 2 )

    return result


def build_datatable_json( request, objects, info ):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param: request
    :param: objects
    :param: info
    :return: String
    """

    # options set
    list_display = info['fields_to_select']
    list_filter = info['fields_to_search']
    default_order_by = info['default_order_by']

    # count total items:
    total_records = objects.count()

    #filter on list_filter using __contains
    if request.method == 'GET' and 'sSearch' in request.GET:
        search = request.GET['sSearch']
        queries = [Q(**{f+'__contains' : search}) for f in list_filter]
        qs = reduce(lambda x, y: x|y, queries)
        objects = objects.filter(qs)

    #sorting
    order = dict( enumerate(list_display) )
    dirs = {'asc': '', 'desc': '-'}
    if request.method == 'GET' and 'sSortDir_0' in request.GET:
        field = order[int(request.GET['iSortCol_0'])]
        if '.' in field:
            field = field.replace( '.', '__' )
        order_by = dirs[request.GET['sSortDir_0']] + field
    else:
        order_by = default_order_by
    objects = objects.order_by( order_by )

    # count items after filtering:
    total_display_records = objects.count()

    # finally, slice according to length sent by dataTables:
    if request.method == 'GET' and 'iDisplayStart' in request.GET:
        start = int( request.GET['iDisplayStart'] )
    else:
        start = 0
    if request.method == 'GET' and 'iDisplayLength' in request.GET:
        length = int(request.GET['iDisplayLength'])
    else:
        length = 10
    objects = objects[ start : (start+length)]

    # build HTML for action buttons (delete, edit, view)
    base_buttons_html = """
                            <div class="btn-group btn-group-xs">
                                <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">
                                    <i class="fa fa-cog"></i>
                                    <i class="fa fa-caret-down"></i>
                                    <span class="sr-only">Toggle Dropdown</span>
                                </button>
                                <ul class="dropdown-menu left" role="menu">
                                    <li><a href="#details_link#" class=""><i class="fa fa-search"></i>View Details</a></li>
                                    <li><a href="#edit_link#" class=""><i class="fa fa-edit"></i>Edit Data</a></li>
                                    <li><a href="#" onclick="javascript: confirm_delete( '#delete_link#'); "><i class="fa fa-trash-o"></i>Remove</a></li>
                                </ul>
                            </div>
                        """

    # extract information
    data = []
    for obj in objects:
        values = []
        for field in list_display:
            if '.' in field:
                split = field.split( '.' )
                sub_obj = getattr( obj, split[0] )
                values.append( getattr( sub_obj, split[1] ) )
            else:
                values.append( getattr( obj, field ) )
        buttons_html = base_buttons_html.replace( "#details_link#", reverse( 'admin:' + info['url_base_name'] + '_details', args = ( obj.id, ) ) )
        buttons_html = buttons_html.replace( "#edit_link#", reverse( 'admin:' + info['url_base_name'] + '_edit', args = ( obj.id, ) ) )
        buttons_html = buttons_html.replace( "#delete_link#", reverse( 'admin:' + info['url_base_name'] + '_delete', args = ( obj.id, ) ) )
        values.append( buttons_html )
        data.append( values )

    # sEcho variable
    if request.method == 'GET' and 'sEcho' in request.GET:
        sEcho = request.GET['sEcho']
    else:
        sEcho = ''

    #define response
    response = {
        'aaData': data,
        'iTotalRecords': total_records,
        'iTotalDisplayRecords': total_display_records,
        'sEcho':  sEcho
    }

    #serialize to json
    s = StringIO()
    json.dump( response, s )
    s.seek( 0 )
    return s.read()


def get_object_or_false( klass, *args, **kwargs ):
    """
    Uses get() to return an object, or False if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), an MultipleObjectsReturned will be raised if more than one
    object is found.
    """
    if 'no_query' in kwargs:
        try:
            return klass
        except UserPersonal.DoesNotExist:
            return False
    else:
        queryset = _get_queryset( klass )
        try:
            return queryset.get( *args, **kwargs )
        except queryset.model.DoesNotExist:
            return False


def get_list_or_false( klass, *args, **kwargs ):
    """
    Uses filter() to return a list of objects, or False if
    the list is empty.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the filter() query.
    """
    queryset = _get_queryset( klass )
    obj_list = list( queryset.filter( *args, **kwargs ) )
    if not obj_list:
        return False
    return obj_list


def get_months_duration_tuple():
    """
    Returns a tuple of records with months/years for work duration
    :return: String
    """
    result = []
    for months in range( 6, 126, 6 ):
        years = months / 12
        if years.is_integer():
            years = int( years )
        if years < 1:
            label = _( '6 months' )
        elif years == 1:
            label = _( '1 year' )
        elif years == 10:
            label = _( '10 years or more' )
        else:
            label = _( '%s years' ) % ( years )
        result.append( ( months, label ) )
    return tuple( [( '', _( 'Select Duration' ) )] + result  )


def get_country_points_css_class( percentage ):
    """
    Returns the css class for the approximate percentage for user country points
    :param: points
    :param: css_class_color
    :return: String
    """

    # If zero, return empty css class
    if percentage == 0:
        return 'orange6'

    # if it's 100% full
    if percentage >= 100:
        return 'green96'

    # These are the percentages defined by css classes in 'style.css'
    possible_percentages = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]

    # Define the color of the bar
    if percentage <= 30:
        color = 'orange'
    elif percentage <= 70:
        color = 'yellow'
    else:
        color = 'green'

    # We will find the nearest number on the possible list to represent it
    list_size = len( possible_percentages )
    for count in range( 0, list_size ):
        if percentage < possible_percentages[count]:
            if count == 0:
                return color + str( possible_percentages[count] )
            else:
                return color + str( possible_percentages[count-1] )
        elif ( count + 1 ) == list_size:
            return color + str( possible_percentages[count-1] )

    return ''

def get_user_progress_css_class( percentage ):
    """
    Returns the css class for the approximate percentage for user registration data
    :param: points
    :param: css_class_color
    :return: String
    """

    # If zero, return the minimum class
    if percentage == 0:
        return 'progressFillDarkOrange progressFillSize5'

    # if it's 100% full
    if percentage >= 100:
        return 'progressFillGreen progressFillSize100'

    # These are the percentages defined by css classes in 'style.css'
    possible_percentages = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

    # Define the color of the bar
    if percentage <= 25:
        color = 'progressFillDarkOrange progressFillSize'
    elif percentage <= 50:
        color = 'progressFillOrange progressFillSize'
    elif percentage <= 75:
        color = 'progressFillYellow progressFillSize'
    else:
        color = 'progressFillGreen progressFillSize'

    # We will find the nearest number on the possible list to represent it
    list_size = len( possible_percentages )
    for count in range( 0, list_size ):
        if percentage < possible_percentages[count]:
            if count == 0:
                return color + str( possible_percentages[count] )
            else:
                return color + str( possible_percentages[count-1] )
        elif ( count + 1 ) == list_size:
            return color + str( possible_percentages[count-1] )

    return ''



###########################
# DEBUGGING FUNCTIONS 
###########################
def dbg( var ):
    """
    Show all 'var' content.
    :param: var The variable to be debugged.
    """

    # Predefined constants
    NEWLINE =  "<br>"
    TAB = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    
    
    # is an instance of a django model?
    if isinstance( var, models.Model ):

        # Get all members of the class excluding functions and __etc__.
        members = [ attr for attr in dir(var) if not callable(attr) and not attr.startswith("__") ]

        debug_str = "[ {0} ( {1} attributes ) ] :{2}".format( var.__class__.__name__, len( members ), NEWLINE )

        for m in members:
            debug_str += TAB + m + NEWLINE
    
    # is list, tuple, dict or set?
    elif type( var ) in ( list, tuple, dict, set ):

        debug_str = "[ {0} ( {1} attributes ) ] :{2}".format( var.__class__.__name__, len( var ), NEWLINE )

        # Shows all key-values of var.
        for k,v in var.items():
            debug_str += "{0}[ {1} ] : {2}{3}".format( TAB, k, v, NEWLINE )
    # is a primitive...
    else:
        debug_str += "({0}) {1}".format( type(var), str( var ) )

    return HttpResponse( debug_str )

