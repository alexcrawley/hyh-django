from django.conf.urls import url

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    url(r'^api-token-auth/',
        ObtainAuthToken.as_view(), name='api_token_auth'),
]
