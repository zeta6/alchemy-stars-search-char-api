# Generated by Django 3.2.6 on 2021-08-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210813_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='asd', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]