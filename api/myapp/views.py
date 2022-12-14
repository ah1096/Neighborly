from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get', 'post']

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    http_method_names = ['get', 'post', 'put']

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    http_method_names = ['get', 'post', 'put']

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete', 'patch']

    def perform_create(self, serializer):
        user = CustomUser.objects.get(id=self.request.data["author"])
        serializer.save(author=user)
    

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def perform_create(self, serializer):
        user = CustomUser.objects.get(id=self.request.data["author"])
        serializer.save(author=user)
    
class ExchangeViewSet(ModelViewSet):
    queryset = Exchange.objects.all()
    serializer_class = ExchangeSerializer
    http_method_names = ['get', 'post', 'put']


class TaggedPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['exTag__exchange_tag']


