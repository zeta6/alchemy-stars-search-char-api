from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.skill_id, filename)

class ActiveSkill(models.Model):
     
    skill_id = models.OneToOneField("Character", verbose_name="active skill", on_delete=models.CASCADE, db_column="active_skill")
    name = models.CharField(max_length=100)
    cooltime = models.PositiveSmallIntegerField()
    preemtive = models.CharField(max_length=4)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)
    text = models.TextField()
    brth_skill_1_br = models.PositiveSmallIntegerField(default=7)
    brth_skill_2_br = models.PositiveSmallIntegerField(default=7)
    asc0_brth_skill_1_cooltime = models.PositiveSmallIntegerField()
    asc0_brth_skill_1_preemptive = models.CharField(max_length=4)
    asc0_brth_skill_1_text = models.TextField()
    asc0_brth_skill_2_cooltime = models.PositiveSmallIntegerField()
    asc0_brth_skill_2_preemptive = models.CharField(max_length=4)
    asc0_brth_skill_2_text = models.TextField()
    asc2_brth_skill_0_cooltime = models.PositiveSmallIntegerField()
    asc2_brth_skill_0_preemptive = models.CharField(max_length=4)
    asc2_brth_skill_0_text = models.TextField()
    asc2_brth_skill_1_cooltime = models.PositiveSmallIntegerField()
    asc2_brth_skill_1_preemptive = models.CharField(max_length=4)
    asc2_brth_skill_1_text = models.TextField()
    asc2_brth_skill_2_cooltime = models.PositiveSmallIntegerField()
    asc2_brth_skill_2_preemptive = models.CharField(max_length=4)
    asc2_brth_skill_2_text = models.TextField()
    asc3_brth_skill_0_cooltime = models.PositiveSmallIntegerField()
    asc3_brth_skill_0_preemptive = models.CharField(max_length=4)
    asc3_brth_skill_0_text = models.TextField()
    asc3_brth_skill_1_cooltime = models.PositiveSmallIntegerField()
    asc3_brth_skill_1_preemptive = models.CharField(max_length=4)
    asc3_brth_skill_1_text = models.TextField()
    asc3_brth_skill_2_cooltime = models.PositiveSmallIntegerField()
    asc3_brth_skill_2_preemptive = models.CharField(max_length=4)
    asc3_brth_skill_2_text = models.TextField()
    
    class Meta:
        verbose_name = "active skill"
        verbose_name_plural = "active skills"
    
    def __str__(self):
        return self.name
