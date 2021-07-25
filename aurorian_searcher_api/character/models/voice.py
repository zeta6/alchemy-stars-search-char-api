from django.db import models

class State(models.Model):

    voice_id = models.OneToOneField("Character", related_name="voice", on_delete=models.CASCADE, db_column="voice")
    name =  models.CharField(max_length=100)

    class Meta:
        verbose_name ="voice"
        verbose_name_plural = "voices"