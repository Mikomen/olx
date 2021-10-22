from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class MadelViewSet(viewsets.ModelViewSet):
    queryset = Madel.objects.all()
    serializer_class = MadelSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    def list(self, request, *args, **kwargs):
        self.serializer_class = CarFullSerializer
        return super().list(self, request, *args, **kwargs)
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CarFullSerializer
        return super().retrieve(self, request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class AdsViewSet(viewsets.ModelViewSet):
    queryset = Ads.objects.all()
    serializer_class =AdsSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()