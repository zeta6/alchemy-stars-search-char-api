# Generated by Django 3.2.6 on 2021-08-13 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210813_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='acces_token',
            new_name='access_token',
        ),
    ]
