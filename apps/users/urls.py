from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^api-token-auth/',
        ObtainAuthToken.as_view(), name='api_token_auth'),

    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
        )
]
