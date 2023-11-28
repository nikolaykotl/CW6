from django.db import models

from client.models import Client

from config import settings

NULLABLE = {'blank': True, 'null': True}

class SettingsMailing(models.Model):
    DAILY = 'раз в день'
    WEEKLY = 'раз в неделю'
    MONTHLY = 'раз в месяц'

    USER_CHOICE = ((DAILY,'раз в день'), (WEEKLY,'раз в неделю'), (MONTHLY, 'раз в месяц'),)

    CREATED = 'Cоздана'
    STARTED = 'Запущена'
    CLOSED = 'Завершена'

    MAILING_STATUS = ((CREATED, 'Cоздана'), (STARTED, 'Запущена'), (CLOSED, 'Завершена'))
    date_start = models.DateField(verbose_name='дата начала рассылки')
    date_stop = models.DateField(verbose_name='дата окончания рассылки')
    time_mailing = models.TimeField(verbose_name='время рассылки')
    regularity = models.CharField(max_length=20,choices=USER_CHOICE, default=DAILY, verbose_name='периодичность')
    mailing_status = models.CharField(max_length=20,choices=MAILING_STATUS, default=CREATED, verbose_name='статус рассылки')
    def __str__(self):
        return f'{self.regularity}'
    class Meta():
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class Messages(models.Model):
    FORSEND = 'К отправке'
    SENT = 'Отправлено'

    CHOICES = [
        (FORSEND, "К отправке"),
        (SENT, "Отправлено"),
    ]
    title = models.CharField(max_length=250,unique=True, verbose_name='тема письма')
    body = models.TextField(verbose_name='содержание')
    date_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    time_create = models.TimeField(auto_now_add=True, verbose_name='время создания')
    status = models.CharField(max_length=50, choices=CHOICES, verbose_name='статус', blank=True)
    setting = models.ForeignKey(SettingsMailing, on_delete=models.CASCADE, verbose_name='настройки')
    is_active = models.BooleanField(default=True, verbose_name='активная')
    clients = models.ManyToManyField(Client)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return  f'Тема: {self.title}, содержание: {self.body}, статус отправки: {self.status}, {self.clients}'

    class Meta():
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

class Logs(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )
    date = models.DateField(auto_now_add=True, verbose_name='дата попытки')
    time = models.TimeField(auto_now_add=True, verbose_name='время попытки')
    status = models.CharField(max_length=20, choices=STATUSES, default='Успешно', verbose_name='статус')
    server_response = models.TextField(verbose_name='ответ сервера', blank=True)
    message = models.ForeignKey(Messages, on_delete=models.CASCADE, related_name='logs', verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')