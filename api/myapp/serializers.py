from rest_framework import serializers
from .models import *
from .fields import *


#https://www.youtube.com/watch?v=YZN_HDtsRLc&t=136s&ab_channel=BootcampVideos
#https://www.geeksforgeeks.org/axios-in-react-a-guide-for-beginners/


class SkillSerializer(serializers.ModelSerializer):
    # user_list = NameListingField(many=True, read_only=True)
    class Meta:
        model = Skill
        fields = ('id', 'skill',)

class LocationSerializer(serializers.ModelSerializer):
    # user_list = NameListingField(many=True, read_only=True)
    class Meta:
        model = Location
        fields = ('id','location')

class RoleSerializer(serializers.ModelSerializer):
    # user_list = NameListingField(many=True, read_only=True)
    class Meta:
        model = Role
        fields = ('id','role')


class ExchangeSerializer(serializers.ModelSerializer):
    # user_list = NameListingField(many=True, read_only=True)
    class Meta:
        model = Exchange
        fields = ('id','exchange_tag')

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = (
                'id',
                'content',
                'author',
                'created_at', 
                'post'
                )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True,read_only=True)
    exTag = ExchangeField(many=False, required=False, queryset=Exchange.objects.all())
    class Meta:
        model = Post
        fields = (
                'id',
                'content',
                'author',
                'created_on',
                'comments',
                'exTag'
                )


class UserSerializer(serializers.ModelSerializer):
    skills = SkillField(many=True, required=False, queryset=Skill.objects.all())
    location = LocationField(many=False, required=False, queryset=Location.objects.all())
    role = RoleField(many=False, required=False, queryset=Role.objects.all())
    user_post = PostSerializer(many=True, required=False)

    class Meta: 
        model = CustomUser
        fields = ('email', 'id', 'is_staff', 'username', 'password', 'first_name', 'last_name', 'biotext', 'skills', 'location', 'role', 'user_post') 
        """ 
        only pull in the PROVIDED DJANGO USER FIELDS that are going to be used in creating a user, 
        and then add your extended fields,
        '__all__' pulls in all fields and creates an error for the validation step below
        """
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        skills_data = validated_data.pop('skills', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        
        
        if password is not None:
            instance.set_password(password)
        instance.save()

        if skills_data:
            for skill in skills_data:
                instance.skills.add(skill)

        return instance





