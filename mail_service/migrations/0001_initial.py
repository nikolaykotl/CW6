# Generated by Django 4.2.7 on 2023-11-19 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата попытки')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='время попытки')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], default='Успешно', max_length=20, verbose_name='статус')),
                ('server_response', models.TextField(blank=True, verbose_name='ответ сервера')),
            ],
        ),
        migrations.CreateModel(
            name='SettingsMailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='дата начала рассылки')),
                ('date_stop', models.DateField(verbose_name='дата окончания рассылки')),
                ('time_mailing', models.TimeField(verbose_name='время рассылки')),
                ('regularity', models.CharField(choices=[('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц')], default='раз в день', max_length=20, verbose_name='периодичность')),
                ('mailing_status', models.CharField(choices=[('Cоздана', 'Cоздана'), ('Запущена', 'Запущена'), ('Завершена', 'Завершена')], default='Cоздана', max_length=20, verbose_name='статус рассылки')),
            ],
            options={
                'verbose_name': 'настройка',
                'verbose_name_plural': 'настройки',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='содержание')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('time_create', models.TimeField(auto_now_add=True, verbose_name='время создания')),
                ('status', models.CharField(blank=True, choices=[('К отправке', 'К отправке'), ('Отправлено', 'Отправлено')], max_length=50, verbose_name='статус')),
                ('clients', models.ManyToManyField(to='client.client')),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail_service.settingsmailing', verbose_name='настройки')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
    ]
