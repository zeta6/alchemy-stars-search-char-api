from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.skill_id, filename)

class ChainSkill(models.Model):
     
    skill_id = models.OneToOneField("Character", verbose_name="chain skill", on_delete=models.CASCADE, db_column="chain_skill")
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)
    lv1_tiles = models.PositiveSmallIntegerField()
    lv1_text = models.TextField()
    lv2_tiles = models.PositiveSmallIntegerField()
    lv2_text = models.TextField()
    lv3_tiles = models.PositiveSmallIntegerField()
    lv3_text = models.TextField()

    class Meta:
        verbose_name = "chain skill"
        verbose_name_plural = "chain skills"
    
    def __str__(self):
        return self.name