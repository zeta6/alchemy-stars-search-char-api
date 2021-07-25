from django.db import models

class Breakthrough(models.Model):
     
    brth_id = models.OneToOneField("Character", verbose_name="breakthrough", on_delete=models.CASCADE, db_column="breakthrough")
    count_1 = models.TextField()
    count_2 = models.TextField()
    count_3 = models.TextField()
    count_4 = models.TextField()
    count_5 = models.TextField()
    count_6 = models.TextField()

    class Meta:
        verbose_name = "breakthrough"
        verbose_name_plural = "breakthroughs"
    
    # def __str__(self):
    #     return self.name