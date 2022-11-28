from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('myapp', UserAPIView.as_view()),
    path('myapp/<str:pk>/', UserAPIView.as_view())
]