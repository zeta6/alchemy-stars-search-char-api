from django.db import models

class RecruitBanner(models.Model):
     
    name = models.CharField(max_length=50,blank=True)  
    image = models.ImageField(upload_to="recruit_images", height_field=None, width_field=None, max_length=None, blank=True)  
    char_id_not_included = models.TextField(blank=True)

    class Meta:
        verbose_name = "Recruit banner"
        verbose_name_plural = "Recruit banner"

    def __str__(self):
        return self.name