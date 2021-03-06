from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.post_details, name='post_details'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^article/(?P<pk>[0-9])/edit/$', views.post_edit, name='post_edit'),
]
