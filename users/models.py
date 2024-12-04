from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    photo = models.ImageField(upload_to="users_photo/%Y/%m/%d/", blank=True, null=True, verbose_name = "Фото пользователя")


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"