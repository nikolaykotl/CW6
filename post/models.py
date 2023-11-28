from django.db import models

from mail_service.models import NULLABLE
from users.models import User


class Post(models.Model):

    title = models.CharField(max_length=150, verbose_name='название статьи')
    body = models.TextField(verbose_name='содержание статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата и время написания')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='автор')
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    image = models.ImageField(upload_to='post/',verbose_name='изображение', **NULLABLE)
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):

        return self.body

    class Meta():
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'