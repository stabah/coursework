from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiz2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'gistogramm.views.index'),
    url(r'^answer/','gistogramm.views.answer'),
    url(r'^admin/', include(admin.site.urls)),
)
