from django.db import models

class Ascension(models.Model):
     
    asc_id = models.OneToOneField("Character", related_name="ascension", on_delete=models.CASCADE)
    lv1 = models.TextField(blank=True, null=True)
    lv2 = models.TextField(blank=True, null=True)
    lv3 = models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = "ascension"
        verbose_name_plural = "ascensions"

    # def save(self, *args, **kwargs):
    #     self.lv1 = "lv1"
    #     self.lv2 = "lv2"
    #     super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return "ascension"