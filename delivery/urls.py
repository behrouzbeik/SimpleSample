from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('tracking', TrackingViewSet, basename="tracking")

urlpatterns = [
    path('', include(router.urls)),
    # path('status/', views.members, name='status'),
]