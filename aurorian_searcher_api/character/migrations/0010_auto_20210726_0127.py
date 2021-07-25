# Generated by Django 3.2.5 on 2021-07-25 16:27

import character.models.character
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0009_auto_20210726_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=character.models.character.upload_path),
        ),
        migrations.AlterField(
            model_name='state',
            name='attack',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='defence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='hit_point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
