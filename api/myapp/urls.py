from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'locations', LocationViewSet)


urlpatterns = [
    path('', include(router.urls))
]