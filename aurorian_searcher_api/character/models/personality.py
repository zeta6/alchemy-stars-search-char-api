from django.db import models

class Personality(models.Model):
     
    name = models.CharField(max_length=50)  
    icon = models.ImageField(upload_to="personality_icons", height_field=None, width_field=None, max_length=None, null=True, blank=True)  
    small_gift = models.CharField(max_length=100)
    big_gift = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Personality"
        verbose_name_plural = "Personalities"

    def __str__(self):
        return self.name