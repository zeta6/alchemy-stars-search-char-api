from django.db import models


class Faction(models.Model):
     
    name = models.CharField(max_length=50,blank=True)  
    icon = models.ImageField(upload_to="faction_icons", height_field=None, width_field=None, max_length=None, blank=True)  
    small_gift = models.CharField(max_length=100, blank=True)
    big_gift = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Faction"
        verbose_name_plural = "Factions"

    def __str__(self):
        return self.name