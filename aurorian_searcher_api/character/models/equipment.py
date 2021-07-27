from django.db import models

def upload_path(instance, filename):
    return '{0}/equipment_image/{1}'.format(instance.equip_id, filename)

class Equipment(models.Model):
     
    equip_id = models.OneToOneField("Character", related_name="equipment", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    lv1_text = models.TextField(blank=True, null=True)
    lv3_text = models.TextField(blank=True, null=True)
    lv6_text = models.TextField(blank=True, null=True)
    lv10_text = models.TextField(blank=True, null=True)
    lv1_state_text = models.TextField(blank=True, null=True)
    lv2_state_text = models.TextField(blank=True, null=True)
    lv4_state_text = models.TextField(blank=True, null=True)
    lv5_state_text = models.TextField(blank=True, null=True)
    lv7_state_text = models.TextField(blank=True, null=True)
    lv8_state_text = models.TextField(blank=True, null=True)
    lv9_state_text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "equipment input only name, image, text"
        verbose_name_plural = "equipments"

    def save(self, *args, **kwargs):
        if self.lv1_state_text == "":
            self.lv1_state_text = "공격력+30, 방어력+10, HP+50, 유리한 속성 데미지 3%"
        if self.lv2_state_text == "":
            self.lv2_state_text = "공격력+60, 방어력+20, HP+100, 유리한 속성 데미지 7%"
        if self.lv4_state_text == "":
            self.lv4_state_text = "공격력+90, 방어력+30, HP+200, 유리한 속성 데미지 11%"
        if self.lv5_state_text == "":
            self.lv5_state_text = "공격력+120, 방어력+40, HP+300, 유리한 속성 데미지 15%"
        if self.lv7_state_text == "":
            self.lv7_state_text = "공격력+170, 방어력+55, HP+450, 유리한 속성 데미지 20%"
        if self.lv8_state_text == "":
            self.lv8_state_text = "공격력+220, 방어력+70, HP+600, 유리한 속성 데미지 25%"
        if self.lv9_state_text == "":
            self.lv9_state_text = "공격력+270, 방어력+85, HP+750, 유리한 속성 데미지 30%"
        self.lv1_text = self.equip_id.equip_skill.lv1_text
        self.lv3_text = self.equip_id.equip_skill.lv3_text
        self.lv6_text = self.equip_id.equip_skill.lv6_text
        self.lv10_text = self.equip_id.equip_skill.lv10_text
        super().save(*args, **kwargs)
   
    def __str__(self):
        return self.name