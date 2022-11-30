from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserAPIView)
router.register(r'skills', SkillAPIView)


urlpatterns = [
    path('myapp', UserAPIView.as_view()),
    path('myapp/<str:pk>/', UserAPIView.as_view())
]