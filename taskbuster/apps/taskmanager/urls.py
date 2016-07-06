from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^tasks/$', views.post_list),
    url(r'^task_detail/(?P<pk>[0-9]+)/$', views.task_detail,
        name='task_detail'),
]
