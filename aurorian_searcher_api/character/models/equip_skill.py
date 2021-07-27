from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.skill_id, filename)

class EquipSkill(models.Model):
     
    skill_id = models.OneToOneField("Character", related_name="equip_skill", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    lv1_text = models.TextField(blank=True, null=True)
    lv3_text = models.TextField(blank=True, null=True)
    lv6_text = models.TextField(blank=True, null=True)
    lv10_text = models.TextField(blank=True, null=True)
    asc2_enhance = models.BooleanField(default=False)
    asc2_lv1_text = models.TextField(blank=True, null=True)
    asc2_lv3_text = models.TextField(blank=True, null=True)
    asc2_lv6_text = models.TextField(blank=True, null=True)
    asc2_lv10_text = models.TextField(blank=True, null=True)
    asc3_enhance = models.BooleanField(default=False)
    asc3_lv1_text = models.TextField(blank=True, null=True)
    asc3_lv3_text = models.TextField(blank=True, null=True)
    asc3_lv6_text = models.TextField(blank=True, null=True)
    asc3_lv10_text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "equip skill input name, icon, texts, enhanced skill"
        verbose_name_plural = "equip skills"

    def save(self, *args, **kwargs):
        if self.asc2_enhance == False:
            self.asc2_lv1_text = self.lv1_text
            self.asc2_lv3_text = self.lv3_text
            self.asc2_lv6_text = self.lv6_text
            self.asc2_lv10_text = self.lv10_text
        if self.asc3_enhance == False:
            self.asc3_lv1_text = self.asc2_lv1_text
            self.asc3_lv3_text = self.asc2_lv3_text
            self.asc3_lv6_text = self.asc2_lv6_text
            self.asc3_lv10_text = self.asc2_lv10_text
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name