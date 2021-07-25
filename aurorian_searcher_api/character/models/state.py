from django.db import models

class State(models.Model):

    state_id = models.OneToOneField("Character", related_name="state", on_delete=models.CASCADE, db_column="state")
    attack = models.IntegerField()
    defence = models.IntegerField()
    hit_point = models.IntegerField()

    class Meta:
        verbose_name ="state"
        verbose_name_plural = "states"