from django.db import models

class State(models.Model):

    state_id = models.OneToOneField("Character", related_name="state", on_delete=models.CASCADE)
    attack = models.IntegerField(blank=True, null=True)
    defence = models.IntegerField(blank=True, null=True)
    hit_point = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name ="state"
        verbose_name_plural = "states"