from django.db import models

class Breakthrough(models.Model):
     
    brth_id = models.OneToOneField("Character", related_name="breakthrough", on_delete=models.CASCADE)
    count_1 = models.TextField(null=True,blank=True)
    count_2 = models.TextField(null=True,blank=True)
    count_3 = models.TextField(null=True,blank=True)
    count_4 = models.TextField(null=True,blank=True)
    count_5 = models.TextField(null=True,blank=True)
    count_6 = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "breakthrough"
        verbose_name_plural = "breakthroughs"
    
    # def __str__(self):
    #     return self.name