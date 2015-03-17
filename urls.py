from django.conf.urls import patterns, include, url
from django.contrib import admin


from apps.views import LandingPageView
from apps import api_urls


urlpatterns = patterns(
    '',
    url(r'^$', LandingPageView.as_view(), name='home'),
    url(r'^api/', include(api_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
