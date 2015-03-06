from django.http import HttpResponseRedirect, Http404, HttpResponse

# Create your views here.


def list_post( request ):

    return HttpResponse( 'test' )