# Generated by Django 4.2.7 on 2023-11-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='адрес электронной почты')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='отчество')),
                ('comment', models.CharField(blank=True, max_length=200, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]