# Generated by Django 4.2.7 on 2023-11-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_service', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активная'),
        ),
    ]
