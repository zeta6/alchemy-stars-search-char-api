from django.db import models

class Ascension(models.Model):
     
    asc_id = models.OneToOneField("Character", verbose_name="ascension", on_delete=models.CASCADE, db_column="ascension")
    lv1 = models.TextField()
    lv2 = models.TextField()
    lv3 = models.TextField()
    

    class Meta:
        verbose_name = "ascension"
        verbose_name_plural = "ascensions"
    
    # def __str__(self):
    #     return self.name