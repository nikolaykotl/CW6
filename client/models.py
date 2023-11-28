from django.db import models

#from mail_service.models import Messages

NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='адрес электронной почты')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    patronymic = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    comment = models.CharField(max_length=200, verbose_name='комментарий', **NULLABLE)
#    messages = models.ForeignKey(Messages, on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
     #   return f'Клиент: {self.last_name} {self.first_name} \nemail: {self.email}; '
        return self.email

    class Meta():
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'