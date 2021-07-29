from django.db import models

class State(models.Model):

    state_id = models.OneToOneField("Character", related_name="state", on_delete=models.CASCADE)
    attack = models.CharField(max_length=6, blank=True)
    defence = models.CharField(max_length=6, blank=True)
    hit_point = models.CharField(max_length=6, blank=True)

    class Meta:
        verbose_name ="state"
        verbose_name_plural = "states"