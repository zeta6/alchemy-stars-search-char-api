from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.equip_skill_id, filename)

class EquipSkill(models.Model):
     
    equip_skill_id = models.OneToOneField("Character", related_name="equip_skill", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True)
    lv1_text = models.TextField(blank=True)
    lv3_text = models.TextField(blank=True)
    lv6_text = models.TextField(blank=True)
    lv10_text = models.TextField(blank=True)
    br1_up = models.BooleanField(default=False)
    br2_up = models.BooleanField(default=False)
    asc2_up = models.BooleanField(default=False)
    asc3_up = models.BooleanField(default=False)

    class Meta:
        verbose_name = "equip skill input name, icon, texts, enhanced skill"
        verbose_name_plural = "equip skills"

    # def save(self, *args, **kwargs):
    #     if self.asc2_enhance == False:
    #         self.asc2_lv1_text = self.lv1_text
    #         self.asc2_lv3_text = self.lv3_text
    #         self.asc2_lv6_text = self.lv6_text
    #         self.asc2_lv10_text = self.lv10_text
    #     if self.asc3_enhance == False:
    #         self.asc3_lv1_text = self.asc2_lv1_text
    #         self.asc3_lv3_text = self.asc2_lv3_text
    #         self.asc3_lv6_text = self.asc2_lv6_text
    #         self.asc3_lv10_text = self.asc2_lv10_text
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name