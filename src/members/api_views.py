from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

class MemberTagViewset(viewsets.ModelViewSet):
    queryset = models.MemberTag.objects.all()
    serializer_class=serializers.MemberTagSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set

class MemberViewset(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class=serializers.MemberSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set
    

class ClubViewset(viewsets.ModelViewSet):
    queryset = models.Club.objects.all()
    serializer_class=serializers.ClubSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set