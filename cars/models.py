from django.db import models
from django.contrib.auth.models import User


class Mark(models.Model):
    name = models.CharField(max_length=255, verbose_name="Марка")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Марка"
        verbose_name_plural = "Марки"


class Madel(models.Model):
    marks = models.ForeignKey(Mark, verbose_name="Марка", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Модель", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

class Color(models.Model):
    name = models.CharField(verbose_name="Цвет", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Цвет"
        verbose_name_plural = "Цветы"

class Car(models.Model):
    marka = models.ForeignKey(Mark, verbose_name="Марка", on_delete=models.PROTECT)
    madel = models.ForeignKey(Madel, verbose_name="Модель", on_delete=models.PROTECT)
    color = models.ForeignKey(Color, verbose_name="Цвет", on_delete=models.PROTECT)

    def __str__(self):
        return self.marka.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Ads(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Называния рекламы", max_length=255)
    car = models.ForeignKey(Car, verbose_name="Автомобиль", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    text = models.CharField(verbose_name="Коментарии", max_length=500)
    ads = models.ForeignKey(Ads, verbose_name="Реклама", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = "Комментария"
        verbose_name_plural = "Комментарии"

