from django.conf.urls import patterns, include, url
from . import views


urlpatterns = [
    url(r'^gen-samples/$', views.gen_samples, name='gen_samples'),
    url(r'^insert/$', views.run_multi_tuple_insert, name='run_multi_tuple_insert'),
]
