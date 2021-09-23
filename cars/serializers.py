from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'id']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name', 'id']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'name']

class MadelSerializer(serializers.ModelSerializer):
    marks = MarkSerializer(read_only=True, many=True)
    class Meta:
        model = Madel
        fields = ['id', 'name', 'marks']

class CarSerializer(serializers.ModelSerializer):

    marka = MarkSerializer()
    model = MadelSerializer()
    color = ColorSerializer()

    class Meta:
        model = Car
        fields = [ 'id', 'marka', 'model', 'color',]

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ['author', 'text']

class AdsSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comment = CommentSerializer
    car = CarSerializer
    class Meta:
        model = Ads
        fields = ['author', 'comment', 'car']
