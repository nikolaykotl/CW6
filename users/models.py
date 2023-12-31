from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from client.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=20,verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    is_block =  models.BooleanField(default=False, verbose_name='заблокирован')

    email_verify = models.BooleanField(default=False, verbose_name='верификация email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []