import django
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello from Django %s." % (django.get_version(),))