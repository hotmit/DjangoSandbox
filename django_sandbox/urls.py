from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django_sandbox.apps.home.views import view_homepage


urlpatterns = [
    url(r'^$', view_homepage, name='home_page'),
    url(r'^multi-tuple/', include('django_sandbox.apps.multi_tuple_insert.urls', namespace='multi_tuple')),
    url(r'^multi-key/', include('django_sandbox.apps.multi_keys_filter.urls', namespace='multi_key')),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
