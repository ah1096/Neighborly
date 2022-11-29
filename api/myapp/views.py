from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response

class UserAPIView(APIView):

# get one user
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

# get all users; READ
    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = UserSerializer(data)
            
        else:
            data = CustomUser.objects.all()
            serializer = UserSerializer(data, many=True)

        return Response(serializer.data)
            
# create a new user
    def post(self, request, format=None):
        print('You sent a post request')
        data = request.data
        serializer = UserSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': "User created successfully",
            'data': serializer.data,
        }

        return response

#update user
    def put(self, request, pk=None, format=None):
        print('UPDATE')
        user_to_update = CustomUser.objects.get(pk=pk)
        data = request.data
        serializer = UserSerializer(instance=user_to_update, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message' : 'Profile updated successfully',
            'data' : serializer.data
        }

        return response

#delete user/deactivate account
    def delete(self, request, pk, format=None):
        user_to_delete = self.get_object(pk=pk)
        user_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
