from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views



router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    
    path('', include(router.urls)),
]