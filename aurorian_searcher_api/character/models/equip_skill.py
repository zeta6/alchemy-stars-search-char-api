from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.skill_id, filename)

class EquipSkill(models.Model):
     
    skill_id = models.OneToOneField("Character", verbose_name="equip skill", on_delete=models.CASCADE, db_column="equip_skill")
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)
    lv1_text = models.TextField()
    lv3_text = models.TextField()
    lv6_text = models.TextField()
    lv10_text = models.TextField()
    asc2_enhance = models.BooleanField(default=False)
    asc2_lv1_text = models.TextField(null=True)
    asc2_lv3_text = models.TextField(null=True)
    asc2_lv6_text = models.TextField(null=True)
    asc2_lv10_text = models.TextField(null=True)
    asc3_enhance = models.BooleanField(default=False)
    asc3_lv1_text = models.TextField(null=True)
    asc3_lv3_text = models.TextField(null=True)
    asc3_lv6_text = models.TextField(null=True)
    asc3_lv10_text = models.TextField(null=True)

    class Meta:
        verbose_name = "equip skill"
        verbose_name_plural = "equip skills"
    
    def __str__(self):
        return self.name