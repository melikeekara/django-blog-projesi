from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    def __str__(self):
        return self.username
