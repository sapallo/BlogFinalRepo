from django.contrib.auth.models import AbstractUser
from django.db import models
import os 


def get_avatar_filename(instance, filename):
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f"user_{instance.id}_avatar{file_extension}"
    return os.path.join('user/avatar/',new_filename)

class User(AbstractUser):
    alias = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default='user/default/avatar_default.jpg')
