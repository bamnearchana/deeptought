from rest_framework import routers
from django.urls import path, include
from .views import EventViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('api/v3/app/', include(router.urls)),
]
