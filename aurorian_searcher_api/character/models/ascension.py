from django.db import models

class Ascension(models.Model):
     
    asc_id = models.OneToOneField("Character", related_name="ascension", on_delete=models.CASCADE)
    lv1 = models.TextField(blank=True, null=True)
    lv2 = models.TextField(blank=True, null=True)
    lv3 = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.lv1 = "장비 스킬 개방: " + self.asc_id.equip_skill.lv1_text
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "ascension autoinput = lv1: equip_lv1 text"
        verbose_name_plural = "ascensions"
