# Generated by Django 4.2.7 on 2023-11-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_block',
            field=models.BooleanField(default=False, verbose_name='заблокирован'),
        ),
    ]
