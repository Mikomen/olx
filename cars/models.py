from django.db import models
from django.contrib.auth.models import User


class Mark(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Madel(models.Model):
    marks = models.ForeignKey(Mark, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    marka = models.ForeignKey(Mark, on_delete=models.PROTECT)
    madel = models.ForeignKey(Madel, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    def __str__(self):
        return self.marka.name

class Ads(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=500)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)

