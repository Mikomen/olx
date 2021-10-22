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

    class Meta:
        model = Madel
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'

class CarFullSerializer(serializers.ModelSerializer):
    marka = MarkSerializer()
    class Meta:
        model = Car
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class AdsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = '__all__'

class CarsListSerializer(serializers.ModelSerializer):
    serializer_class = AdsSerializer
    class Meta:
        model = Car
        fields = '__all__'