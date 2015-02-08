import django
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response


def hello(request):
    return HttpResponse("Hello from Django %s." % (django.get_version(),))


class JSONView(APIView):
    def get(self, request, format=None):
        return Response({"hello": "world"})
