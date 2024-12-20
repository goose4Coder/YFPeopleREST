from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from . import models

class MemberTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MemberTag
        fields = ('id', 'title')
