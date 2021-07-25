# Generated by Django 3.2.5 on 2021-07-25 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeskill',
            name='skill_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='active_skill', to='character.character'),
        ),
        migrations.AlterField(
            model_name='chainskill',
            name='skill_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chain_skill', to='character.character'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equip_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='character.character'),
        ),
        migrations.AlterField(
            model_name='equipskill',
            name='skill_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='equip_skill', to='character.character'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='character.character'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='state', to='character.character'),
        ),
    ]
