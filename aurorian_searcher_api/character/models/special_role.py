from django.db import models

class SpecialRole(models.Model):
     
    sp_role_id = models.OneToOneField("Character", related_name="special_role", on_delete=models.CASCADE)
    tile_change = models.BooleanField(default=False)
    tile_reset = models.BooleanField(default=False)
    teleport = models.BooleanField(default=False)
    heal = models.BooleanField(default=False)
    input_check = models.BooleanField(default=False)

    class Meta:
        verbose_name = "special role"
        verbose_name_plural = "special rolose"
    
    # def __str__(self):
    #     return self.name