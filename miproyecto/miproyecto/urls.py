from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout$', 'django.contrib.auth.views.logout'),
    url(r'^update$', 'barrapuntoapp.views.update'),
    url(r'^(.*)$', 'barrapuntoapp.views.cms_users_put'),
)
