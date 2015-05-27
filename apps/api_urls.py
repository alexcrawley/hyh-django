from rest_framework import routers

from django.conf.urls import url, include

from apps.events.views import EventViewSet, EventUserResponseViewSet
from apps.users.views import UserViewSet
from apps.tickets.views import TicketViewSet
from apps.users import urls as users_urls

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'eventuserresponses', EventUserResponseViewSet)
router.register(r'users', UserViewSet)
router.register(r'tickets', TicketViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(users_urls)),

    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
        )
]
