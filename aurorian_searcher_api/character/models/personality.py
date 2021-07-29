from django.db import models

class Personality(models.Model):
     
    name = models.CharField(max_length=50, blank=True)  
    small_gift = models.CharField(max_length=100, blank=True)
    big_gift = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Personality"
        verbose_name_plural = "Personalities"

    def __str__(self):
        return self.name