from django.conf.urls import url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^tasks/$', views.project_list),
    url(r'^add_project_task/$', views.add_project_task, name='add_project_task'),
    url(r'^task_detail/(?P<pk>[0-9]+)/$', views.task_detail,
        name='task_detail'),
    url(r'^close_task/(?P<pk>[0-9]+)/$', views.close_task,
        name='close_task'),
    url(r'^close_project/(?P<pk>[0-9]+)/$', views.close_project,
        name='close_project'),
]
