from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.chain_skill_id, filename)

class ChainSkill(models.Model):
     
    chain_skill_id = models.OneToOneField("Character", related_name="chain_skill", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True)
    lv1_tiles = models.CharField(max_length=4, blank=True)
    lv1_text = models.TextField(blank=True)
    lv2_tiles = models.CharField(max_length=4, blank=True)
    lv2_text = models.TextField(blank=True)
    lv3_tiles = models.CharField(max_length=4, blank=True)
    lv3_text = models.TextField(blank=True)
    br1_up = models.BooleanField(default=False)
    br2_up = models.BooleanField(default=False)
    asc2_up = models.BooleanField(default=False)
    asc3_up = models.BooleanField(default=False)

    class Meta:
        verbose_name = "chain skill"
        verbose_name_plural = "chain skills"
    
    def __str__(self):
        return self.name