from django.db import models

def upload_path(instance, filename):
    return '{0}/equipment_image/{1}'.format(instance.equip_id, filename)

class Equipment(models.Model):
     
    equip_id = models.OneToOneField("Character", related_name="equipment", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    lv1_text = models.TextField(blank=True, null=True)
    lv3_text = models.TextField(blank=True, null=True)
    lv6_text = models.TextField(blank=True, null=True)
    lv10_text = models.TextField(blank=True, null=True)
    lv1_state_text = models.CharField(max_length=200, blank=True, null=True)
    lv2_state_text = models.CharField(max_length=200, blank=True, null=True)
    lv4_state_text = models.CharField(max_length=200, blank=True, null=True)
    lv5_state_text = models.CharField(max_length=200, blank=True, null=True)
    lv7_state_text = models.CharField(max_length=200, blank=True, null=True)
    lv8_state_text = models.CharField(max_length=200, blank=True, null=True)
    lv9_state_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "equipment"
        verbose_name_plural = "equipments"
    
    def __str__(self):
        return self.name