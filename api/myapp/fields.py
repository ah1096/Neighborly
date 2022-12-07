from rest_framework import serializers
from .models import *

class SkillField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.skill

    def to_internal_value(self, data):
        return Skill.objects.get(pk=data)


class LocationField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.location

    def to_internal_value(self, data):
        return Location.objects.get(pk=data)


class RoleField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.role_tag

    def to_internal_value(self, data):
        return Role.objects.get(pk=data)