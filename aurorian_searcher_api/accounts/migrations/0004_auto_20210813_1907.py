# Generated by Django 3.2.6 on 2021-08-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_acces_token_user_access_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='provider_id',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
