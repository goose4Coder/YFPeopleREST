from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from . import models

class MemberTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MemberTag
        fields = ('id', 'title')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = ('id', 'name', 'lastname','email' ,'telegram', 'date_of_birth', 'tags')

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('id', 'title', 'leader', 'members')
