from django.db import models

class Voice(models.Model):

    voice_id = models.OneToOneField("Character", related_name="voice", on_delete=models.CASCADE)
    name =  models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name ="voice"
        verbose_name_plural = "voices"