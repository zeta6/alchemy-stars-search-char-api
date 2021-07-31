from django.urls import reverse
from django.db import models
from .main_attr import MainAttribute
from .sub_attr import SubAttribute
from .char_class import CharClass
from .faction import Faction
from .personality import Personality
from .special_role import SpecialRole

def upload_path(instance, filename):
    return '{0}/icon_logo/{1}'.format(instance.name_alphabet, filename)

class Character(models.Model):
    name = models.CharField(max_length=50)
    name_alphabet = models.CharField(max_length=30)
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True) 
    logo = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True) 
    rarity = models.CharField(max_length=4, blank=True)
    main_attribute = models.ForeignKey("MainAttribute", verbose_name="주속성", on_delete=models.SET_NULL, null=True, blank=True)
    sub_attribute = models.ForeignKey("SubAttribute", verbose_name="부속성", on_delete=models.SET_NULL, null=True, blank=True)
    char_class = models.ForeignKey("CharClass", verbose_name="클래스", on_delete=models.SET_NULL, null=True, blank=True)
    faction = models.ForeignKey("Faction", verbose_name="소속 세력", on_delete=models.SET_NULL, null=True, blank=True)
    personality = models.ForeignKey("Personality", verbose_name="성격", on_delete=models.SET_NULL, null=True, blank=True)
    special_role = models.ForeignKey("SpecialRole", verbose_name="특이사항", on_delete=models.SET_NULL, null=True)
    profile = models.TextField(blank=True)
    #state, image, charin_skill, active_skill, equip_skill, equipment, breakthrough, ascension, voice 
    class Meta:
        verbose_name = "character"
        verbose_name_plural = "characters"

    def __str__(self):
        return self.name_alphabet

    def get_absolute_url(self):
        return reverse("character_detail", args=[self.id])
