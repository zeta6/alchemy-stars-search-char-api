from django.db import models

def upload_path(instance, filename):
    return '{0}/skill_icon/{1}'.format(instance.skill_id, filename)

class ActiveSkill(models.Model):
     
    skill_id = models.OneToOneField("Character", related_name="active_skill", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    cooltime = models.CharField(max_length=6, blank=True)
    preemptive = models.CharField(max_length=4, blank=True)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True)
    text = models.TextField(blank=True)
    br1_up = models.BooleanField(default=False)
    br2_up = models.BooleanField(default=False)
    asc2_up = models.BooleanField(default=False)
    asc3_up = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name = "active skill chanefalse = 하위스킬입력, brth_br=7:강화없음"
        verbose_name_plural = "active skills"

    # def save(self, *args, **kwargs):
    #     if self.brth_skill_1_br == 7:
    #         self.asc0_brth_skill_1_cooltime = self.cooltime
    #         self.asc0_brth_skill_1_preemptive = self.preemptive
    #         self.asc0_brth_skill_1_text = self.text
    #     if self.brth_skill_2_br == 7:
    #         self.asc0_brth_skill_2_cooltime = self.asc0_brth_skill_1_cooltime
    #         self.asc0_brth_skill_2_preemptive = self.asc0_brth_skill_1_preemptive
    #         self.asc0_brth_skill_2_text = self.asc0_brth_skill_1_text
    #     if self.asc2_change == False:
    #         self.asc2_brth_skill_0_cooltime = self.cooltime
    #         self.asc2_brth_skill_0_preemptive = self.preemptive
    #         self.asc2_brth_skill_0_text = self.text
    #         self.asc2_brth_skill_1_cooltime = self.asc0_brth_skill_1_cooltime
    #         self.asc2_brth_skill_1_preemptive = self.asc0_brth_skill_1_preemptive
    #         self.asc2_brth_skill_1_text = self.asc0_brth_skill_1_text
    #         self.asc2_brth_skill_2_cooltime = self.asc0_brth_skill_2_cooltime
    #         self.asc2_brth_skill_2_preemptive = self.asc0_brth_skill_2_preemptive
    #         self.asc2_brth_skill_2_text = self.asc0_brth_skill_2_text
    #     if self.asc3_change == False:
    #         self.asc3_brth_skill_0_cooltime = self.asc2_brth_skill_0_cooltime
    #         self.asc3_brth_skill_0_preemptive = self.asc2_brth_skill_0_preemptive
    #         self.asc3_brth_skill_0_text = self.asc2_brth_skill_0_text
    #         self.asc3_brth_skill_1_cooltime = self.asc2_brth_skill_1_cooltime
    #         self.asc3_brth_skill_1_preemptive = self.asc2_brth_skill_1_preemptive
    #         self.asc3_brth_skill_1_text = self.asc2_brth_skill_1_text
    #         self.asc3_brth_skill_2_cooltime = self.asc2_brth_skill_2_cooltime
    #         self.asc3_brth_skill_2_preemptive = self.asc2_brth_skill_2_preemptive
    #         self.asc3_brth_skill_2_text = self.asc2_brth_skill_2_text
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
