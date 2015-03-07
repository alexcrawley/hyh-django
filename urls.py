from django.conf.urls import patterns, include, url
from django.contrib import admin


from apps.views import EmptyView
from apps.events import urls as event_urls
from apps.users import urls as user_urls


urlpatterns = patterns(
    '',
    url(r'^$', EmptyView.as_view(), name='home'),
    url(r'^users/', include(user_urls)),
    url(r'^events/', include(event_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
