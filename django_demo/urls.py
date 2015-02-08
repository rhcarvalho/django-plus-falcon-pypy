from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_demo.views import JSONView


urlpatterns = patterns('',
    url(r'^$', 'django_demo.views.hello', name='hello'),
    url(r'^json/?$', JSONView.as_view(), name='json'),
    url(r'^admin/', include(admin.site.urls)),
)
