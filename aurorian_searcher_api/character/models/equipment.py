from django.db import models

def upload_path(instance, filename):
    return '{0}/equipment_image/{1}'.format(instance.skill_id, filename)

class Equipment(models.Model):
     
    equip_id = models.OneToOneField("Character", verbose_name="equipment", on_delete=models.CASCADE, db_column="equipment")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)
    text = models.TextField()
    lv1_text = models.TextField()
    lv3_text = models.TextField()
    lv6_text = models.TextField()
    lv10_text = models.TextField()
    lv1_state_text = models.CharField(max_leghth=200)
    lv2_state_text = models.CharField(max_leghth=200)
    lv4_state_text = models.CharField(max_leghth=200)
    lv5_state_text = models.CharField(max_leghth=200)
    lv7_state_text = models.CharField(max_leghth=200)
    lv8_state_text = models.CharField(max_leghth=200)
    lv9_state_text = models.CharField(max_leghth=200)

    class Meta:
        verbose_name = "equipment"
        verbose_name_plural = "equipments"
    
    def __str__(self):
        return self.name