# Generated by Django 3.2.6 on 2021-08-13 10:20

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_user_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='asdf', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
