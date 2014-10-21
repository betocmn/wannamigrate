from functools import reduce
from django.db.models import Q
import json
from io import StringIO
from django.core.urlresolvers import reverse
from django.shortcuts import _get_queryset
from calendar import monthrange
from datetime import date, datetime, timedelta


def calculate_age( birth_date ):
    """
    Calculates age based on birth date

    :param birth_date:
    :return Int:
    """

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

    # fields to select
    #objects = objects.values( *list_display )

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
        order_by = dirs[request.GET['sSortDir_0']] + order[int(request.GET['iSortCol_0'])]
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
    queryset = _get_queryset( klass )
    try:
        return queryset.get( *args, **kwargs )
    except queryset.model.DoesNotExist:
        return False

def get_object_or_false( klass, *args, **kwargs ):
    """
    Uses get() to return an object, or False if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Note: Like with get(), an MultipleObjectsReturned will be raised if more than one
    object is found.
    """
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