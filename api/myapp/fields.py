from rest_framework import serializers
from .models import *


class ForeignKeyField(serializers.PrimaryKeyRelatedField):
    """
    To use:
        class ParentSerializer(ModelSerializer):
            child = ForeignKeyField(queryset=Child.objects.all(), serializer=ChildSerializer)
    """
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')
        super().__init__(**kwargs)
    def use_pk_only_optimization(self):
        return False if self.serializer else True
    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


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


class PostField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.title

    def to_internal_value(self, data):
        return Post.objects.get(pk=data)

class ExchangeField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.exchange_tag

    def to_internal_value(self, data):
        return Exchange.objects.get(id=data)