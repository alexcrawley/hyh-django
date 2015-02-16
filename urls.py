from django.conf.urls import patterns, include, url
from django.contrib import admin


from apps.views import EmptyView

urlpatterns = patterns(
    '',
    url(r'^$', EmptyView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
