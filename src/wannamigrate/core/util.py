"""
Custom functions not elsewhere classified.

We put here all functions that couldn't belong to any module or class.
"""

##########################
# Imports
##########################
import json
import time
import re
import math
import datetime
import itertools
import random
import string
import pendulum
from functools import reduce
from decimal import Decimal, ROUND_DOWN
from datetime import date
from io import StringIO
from stdimage.utils import UploadTo
from django.db import connections
from django.utils.functional import lazy
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.shortcuts import _get_queryset
from wannamigrate.core.templatetags.string_extras import status_colour


##########################
# CLASSES
##########################
class CustomUploadToAutoSlugClassNameDir(UploadTo):
    """
    Custom implementation of UploadToAutoSlugClassNameDir
    See: https://github.com/codingjoe/django-stdimage

    This will upload a file to the class name path + slug + random uuid + ext
    """
    path_pattern = '%(class_name)s'

    def __init__(self, populate_from, **kwargs):
        self.populate_from = populate_from
        super(CustomUploadToAutoSlugClassNameDir, self).__init__(populate_from, **kwargs)

    def __call__(self, instance, filename):
        field_value = getattr(instance, self.populate_from)

        self.kwargs.update({
            'name': "%s-%s" % (slugify(field_value), generate_unique_id()),
        })
        return super(CustomUploadToAutoSlugClassNameDir, self).__call__(instance, filename)


##########################
# FUNCTIONS
##########################
def generate_unique_id():
    """
    Generates unique id similarly to PHP's uniqid (smaller string when uuid is too long)

    :return: String
    """
    m = time.time()
    return '%8x%05x' % (math.floor(m), (m - math.floor(m)) * 1000000)


def generate_random_string(size=6, numbers_only=False, ignore_zeros=False):
    """
    Generates random string containing uppercase letters or numbers.

    Note: This is not guaranteed to be unique, for this, please use UUID

    :param size: int
    :param numbers_only: Boolean
    :param ignore_zeros: Boolean
    :return: String
    """
    if ignore_zeros:
        possible = '123456789'
    else:
        possible = string.digits
    if not numbers_only:
        possible += string.ascii_uppercase
    return ''.join(
        random.SystemRandom().choice(possible) for _ in range(size)
    )


def format_monetary(value):
    """
    Formats value with 2 decimal places

    :param: value
    :return: Decimal
    """
    return Decimal(value).quantize(Decimal('.01'), rounding=ROUND_DOWN)


def remove_non_alphanumeric(value):
    """
    Remove special chars

    :param value: str
    :return: String
    """
    pattern = re.compile('[\W_]+')
    return pattern.sub('', value)


def remove_non_numeric(value):
    """
    Removes non numeric chars

    :param value: str
    :return: String
    """
    pattern = re.compile('[^0-9]')
    return pattern.sub('', value)


def convert_to_cents(number):
    """
    Returns cents from a whole value.

    Example: 10.00 = 1000 |  144.20 = 14420

    :param: number
    :return: Int
    """
    result = Decimal(number * 100).quantize(Decimal('1.'))
    return int(result)


def calculate_gst(value, method='inclusive'):
    """
    Calculates GST out of a value

    :param: value
    :param: method 'inclusive' or 'exclusive'
    :return: Int
    """
    if not value:
        return format_monetary(0.00)
    if method == 'inclusive':
        gst = float(value)/11
    else:
        gst = value * 0.1
    return format_monetary(gst)


def date_today():
    """
    Returns DateTime object of current time

    :return DateTime (Pendulum):
    """
    return pendulum.today()


def date_now():
    """
    Returns DateTime object of current time

    :return DateTime (Pendulum):
    """
    return pendulum.now()


def date_from_datetime(date_object):
    """
    Returns Pendulum object from a datetime object

    :param date_object:
    :return DateTime (Pendulum):
    """

    # If Date, formats and converts to str for json encoding
    if isinstance(date_object, datetime.datetime):
        current_tz = timezone.get_current_timezone()
        date_object = pendulum.instance(date_object).in_timezone(current_tz.zone)

    # If Date, formats and converts to str for json encoding
    elif isinstance(date_object, datetime.date):
        date_object = pendulum.from_date(date_object.year, date_object.month, date_object.day)

    return date_object


def date_from_string(string, str_format='%Y-%m-%d'):
    """
    Returns DateTime object from string

    :param string:
    :param str_format:
    :return DateTime (Pendulum):
    """
    return pendulum.from_format(string, str_format)


def date_from_params(year=None, month=None, day=None, hour=None, minute=None):
    """
    Create a Datetime object by specifying one or more date parts (e.g. day, month, year or hour)

    :param year:
    :param month:
    :param day:
    :param hour:
    :param minute:
    :return:
    """
    current_tz = timezone.get_current_timezone()
    pendulum_date = pendulum.from_date(year, month, day, current_tz.zone)
    time_info = {}
    if hour:
        time_info['hours'] = hour
    if minute:
        time_info['minutes'] = minute
    if time_info:
        pendulum_date = pendulum_date.add(**time_info)
    return pendulum_date


def date_to_string(pendulum_datetime, str_format='%Y-%m-%d %H:%M:%S', formatter='classic'):
    """
    Returns formatted string from datetime object

    :param pendulum_datetime:
    :param str_format:
    :param formatter:
    :return DateTime (Pendulum):
    """
    pendulum_datetime = date_from_datetime(pendulum_datetime)
    return pendulum_datetime.format(str_format, formatter=formatter)


def date_subtract(pendulum_datetime, years=0, months=0, weeks=0, days=0, hours=0,
                  minutes=0, seconds=0, microseconds=0):
    """
    Returns datetime objects subtracted by given arguments

    :param pendulum_datetime:
    :param years:
    :param months:
    :param weeks:
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :param microseconds:
    :return DateTime (Pendulum):
    """
    pendulum_datetime = date_from_datetime(pendulum_datetime)
    return pendulum_datetime.subtract(
        years, months, weeks, days, hours, minutes, seconds, microseconds
    )


def date_add(pendulum_datetime, years=0, months=0, weeks=0, days=0, hours=0,
             minutes=0, seconds=0, microseconds=0):

    """
    Returns datetime objects added by given arguments

    :param pendulum_datetime:
    :param years:
    :param months:
    :param weeks:
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :param microseconds:
    :return DateTime (Pendulum):
    """
    pendulum_datetime = date_from_datetime(pendulum_datetime)
    return pendulum_datetime.add(
        years, months, weeks, days, hours, minutes, seconds, microseconds
    )


def dates_last_month():
    """
    Returns 2 DateTime object from start and end of last month

    :return dict containing DateTime (Pendulum) objects:
    """
    return {
        'start': pendulum.now().start_of('month').subtract(months=1),
        'end': pendulum.now().end_of('month').subtract(months=1),
    }


def date_first_day_of_month():
    """
    Returns DateTime object from string

    :return DateTime (Pendulum):
    """
    return pendulum.now().start_of('month')


def date_first_day_of_week():
    """
    Returns DateTime object from string

    :return DateTime (Pendulum):
    """
    return pendulum.now().start_of('week')


def date_next_from_day(month_day, force_next_month=False, from_date=None):
    """
    Returns DateTime object from the next day of the current month_day given.

    :param month_day:
    :param force_next_month:
    :param from_date:
    :return DateTime (Pendulum):
    """
    if from_date:
        base_date = date_from_datetime(from_date)
    else:
        base_date = pendulum.now()
    if force_next_month or base_date.day > month_day:
        next_month = base_date.add(months=1)
        return pendulum.from_date(next_month.year, next_month.month, month_day)
    else:
        return pendulum.from_date(base_date.year, base_date.month, month_day)


def date_next_business_date(from_date=None):
    """
    Returns next business day

    :param from_date:
    :return DateTime (Pendulum):
    """
    if not from_date:
        pendulum_datetime = pendulum.now()
    else:
        pendulum_datetime = date_from_datetime(from_date)

    next_date = date_add(pendulum_datetime, days=1)
    if not next_date.is_weekday():
        next_date = date_add(next_date, days=1)
        if not next_date.is_weekday():
            next_date = date_add(next_date, days=1)
    return next_date


def calculate_age(birth_date):
    """
    Calculates age based on birth date

    :param birth_date:
    :return Int:
    """
    if not birth_date:
        return 0

    today = date.today()
    return today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def build_datatable_json(request, objects, info, actions=['view', 'edit', 'delete']):
    """
    Generates JSON for the listing (required for the JS plugin www.datatables.net)

    :param request:
    :param objects:
    :param info:
    :param actions:
    :return: String
    """

    # options set
    list_display = info['fields_to_select']
    list_filter = info['fields_to_search']
    default_order_by = info['default_order_by']

    # counts total items:
    total_records = objects.count()

    if request.method == 'GET' and 'sSearch' in request.GET:
        search = request.GET['sSearch']
        queries = [Q(**{f + '__icontains': search}) for f in list_filter]
        qs = reduce(lambda x, y: x | y, queries)
        objects = objects.filter(qs)

    # sorting
    order = dict(enumerate(list_display))
    dirs = {'asc': '', 'desc': '-'}
    if request.method == 'GET' and 'sSortDir_0' in request.GET:
        field = order[int(request.GET['iSortCol_0'])]
        if '.' in field:
            field = field.replace('.', '__')
        order_by = dirs[request.GET['sSortDir_0']] + field
    else:
        order_by = default_order_by
    objects = objects.order_by(order_by)

    # counts items after filtering:
    total_display_records = objects.count()

    # finally, slices accordingly to length sent by dataTables:
    if request.method == 'GET' and 'iDisplayStart' in request.GET:
        start = int(request.GET['iDisplayStart'])
    else:
        start = 0
    if request.method == 'GET' and 'iDisplayLength' in request.GET:
        length = int(request.GET['iDisplayLength'])
    else:
        length = 10
    objects = objects[start: (start+length)]

    # builds HTML for action buttons (delete, edit, view)
    view_action_html = ''
    if 'view' in actions:
        view_action_html = '<li><a href="#details_link#" class="listing-view-details">' \
                           '<i class="fa fa-search"></i>View Details</a></li>'
    edit_action_html = ''
    if 'edit' in actions:
        edit_action_html = '<li><a href="#edit_link#" class=""><i class="fa fa-edit"></i>' \
                           'Edit Data</a></li>'
    delete_action_html = ''
    if 'delete' in actions:
        delete_action_html = '<li><a class="delete_link" href="#" onclick="javascript: return ' \
                             'confirm_delete(\'#delete_link#\'); "><i class="fa fa-trash-o">' \
                             '</i>Remove</a></li>'
    base_buttons_html = """
                            <div class="btn-group btn-group-xs #disabled-css-class#">
                                <button type="button" class="btn btn-default dropdown-toggle"
                                data-toggle="dropdown">
                                    <i class="fa fa-cog"></i>
                                    <i class="fa fa-caret-down"></i>
                                    <span class="sr-only">Toggle Dropdown</span>
                                </button>
                                <ul class="dropdown-menu left" role="menu">
                                    %s %s %s
                                </ul>
                            </div>
                        """ % (view_action_html, edit_action_html, delete_action_html)

    # extract information
    data = []
    disabled_fields = ['is_enabled', 'is_active']
    for obj in objects:
        values = []
        row_css_class = ''
        for field in list_display:

            field_name = ''
            value = ''

            # If field is a foreign key
            if '.' in field:
                current_obj = obj
                current_field = field
                while '.' in current_field:
                    split = current_field.split('.')
                    sub_obj = getattr(current_obj, split[0])
                    if sub_obj:
                        value = getattr(sub_obj, split[1])
                        field_name = split[1]
                        current_obj = value
                        current_field = current_field.replace('%s.%s' % (split[0], split[1]), '')
                        if current_field[:1] == '.':
                            current_field = current_field.replace('.', '', 1)
                if current_field:
                    value = getattr(current_obj, current_field)
                    field_name = current_field

            # Normal model value
            else:
                value = getattr(obj, field)
                field_name = field

            # If it's a disabled record, add an error css style
            if field_name in disabled_fields and value is False:
                row_css_class = 'listing-row-disabled'

            # If It's the primary key, make link
            if 'id' == field or 'sku_code' in field:
                pre = '#' if field == 'id' else ''
                value = '<a href="%s">%s%s</a>' % (
                    reverse(info['namespace'] + info['url_base_name'] + ':details', args=(obj.id,)),
                    pre, value
                )

            # If Order or subscription Status, add color
            elif field == 'is_fulfilled':
                value = 'Yes' if value is True else 'No'
                value = status_colour(value)

            # If Order or subscription Status, add color
            elif '_status' in field:
                value = status_colour(value)

            # If boolean, adjust the value to a more friendly format
            elif value is True:
                value = 'Yes'
            elif value is False:
                value = 'No'

            # If Date, formats and converts to str for json encoding
            elif isinstance(value, datetime.datetime):
                current_tz = timezone.get_current_timezone()
                pendulum_datetime = pendulum.instance(value).in_timezone(current_tz.zone)
                value = date_to_string(pendulum_datetime, '%d/%m/%Y %-I:%M%p')

            # If Date, formats and converts to str for json encoding
            elif isinstance(value, datetime.date):
                pendulum_date = pendulum.from_date(value.year, value.month, value.day)
                value = date_to_string(pendulum_date, '%d/%m/%Y')

            # If Decimal, converts to str for json encoding
            elif isinstance(value, Decimal):
                value = str(format_monetary(value))

            if value:
                value = str(value)
            values.append(value)

        if 'view' in actions:
            buttons_html = base_buttons_html.replace("#details_link#", reverse(
                info['namespace'] + info['url_base_name'] + ':details', args=(obj.id,)
            ))
        if 'edit' in actions:
            buttons_html = buttons_html.replace("#edit_link#", reverse(
                info['namespace'] + info['url_base_name'] + ':edit', args=(obj.id,)
            ))
        if 'delete' in actions:
            buttons_html = buttons_html.replace("#delete_link#", reverse(
                info['namespace'] + info['url_base_name'] + ':delete', args=(obj.id,)
            ))
        buttons_html = buttons_html.replace("#disabled-css-class#", row_css_class)
        values.append(buttons_html)
        data.append(values)

    # sEcho variable
    if request.method == 'GET' and 'sEcho' in request.GET:
        sEcho = request.GET['sEcho']
    else:
        sEcho = ''

    # defines response
    response = {
        'aaData': data,
        'iTotalRecords': total_records,
        'iTotalDisplayRecords': total_display_records,
        'sEcho':  sEcho
    }

    # serializes to json
    s = StringIO()
    json.dump(response, s)
    s.seek(0)
    return s.read()


def get_object_or_false(klass, *args, **kwargs):
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
        except klass.DoesNotExist:
            return False
    else:
        queryset = _get_queryset(klass)
        try:
            return queryset.get(*args, **kwargs)
        except queryset.model.DoesNotExist:
            return False


def get_list_or_false(klass, *args, **kwargs):
    """
    Uses filter() to return a list of objects, or False if
    the list is empty.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the filter() query.
    """
    queryset = _get_queryset(klass)
    obj_list = list(queryset.filter(*args, **kwargs))
    if not obj_list:
        return False
    return obj_list


def get_sql_queries():
    """
    Print all SQL Queries
    """
    return lazy(
        lambda: list(itertools.chain(*[connections[x].queries for x in connections])),
        list
    )
