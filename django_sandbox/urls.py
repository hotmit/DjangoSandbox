from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^multi-tuple/', include('django_sandbox.apps.multi_tuple_insert.urls', namespace='multi_tuple'))
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
