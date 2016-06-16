from django.conf.urls import include, url
import django.contrib.auth.views
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from .views import home, home_files

admin.autodiscover()

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout',
        kwargs={'next_page': '/'}),
    url(r'', include('apps.taskmanager.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
