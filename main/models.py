from django.db import models


class Homework(models.Model):
    lesson = models.CharField(max_length=255, verbose_name="Урок")
    content = models.TextField(blank=True, verbose_name="Задание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    deadline = models.DateField(verbose_name="Дедлайн")
