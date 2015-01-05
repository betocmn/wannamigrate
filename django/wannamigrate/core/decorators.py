from functools import wraps
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.decorators import available_attrs


#def restrict_internal_ips( redirect_url = None ):


def restrict_internal_ips( view_func ):
    """
    A view decorator which returns the provided view function,
    modified to return a 403 when the remote address is not in
    the list of internal IPs defined in settings.
    """

    @wraps( view_func, assigned = available_attrs( view_func ) )
    def _wrapped_view( request, *args, **kwargs ):

        x_forwarded_for = request.META.get( 'HTTP_X_FORWARDED_FOR' )
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get( 'REMOTE_ADDR' )
        if ip not in settings.INTERNAL_IPS:
            return HttpResponseRedirect( reverse( 'site:home' ) )
        return view_func( request, *args, **kwargs )

    return _wrapped_view



# Decorator to ensure that the request is accessed over https
def secure_required( view_func ):
    """Decorator that makes sure URL is accessed over https."""
    def _wrapped_view_func( request, *args, **kwargs ):
        if not request.is_secure():
            if getattr(settings, 'HTTPS_SUPPORT', True):
                request_url = request.build_absolute_uri(request.get_full_path())
                secure_url = request_url.replace('http://', 'https://')
                return HttpResponseRedirect(secure_url)
        return view_func( request, *args, **kwargs )
    return _wrapped_view_func