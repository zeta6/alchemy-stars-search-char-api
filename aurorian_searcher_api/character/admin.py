from django.contrib import admin
from .models.character import Character 
from .models.image import Image
from .models.state import State 
from .models.main_attr import MainAttribute
from .models.sub_attr import SubAttribute
from .models.char_class import CharClass
from .models.faction import Faction 
from .models.personality import Personality
from .models.chain_skill import ChainSkill
from .models.active_skill import ActiveSkill
from .models.equip_skill import EquipSkill
from .models.equipment import Equipment
from .models.breakthrough import Breakthrough
from .models.ascension import Ascension
from .models.char_file import CharFile
from .models.voice import Voice
from .models.special_role import SpecialRole

class ImageInline(admin.TabularInline):
    model = Image

class StateInline(admin.TabularInline):
    model = State

class ChainSkillInline(admin.StackedInline):
    model = ChainSkill

class ActiveSkillInline(admin.StackedInline):
    model = ActiveSkill

class EquipSkillInline(admin.StackedInline):
    model = EquipSkill

class EquipmentInline(admin.StackedInline):
    model = Equipment    

class BreakthroughInline(admin.StackedInline):
    model = Breakthrough

class AscensionInline(admin.StackedInline):
    model = Ascension

class SpecialRoleInLine(admin.StackedInline):
    model = SpecialRole

class VoiceInline(admin.TabularInline):
    model = Voice

class CharFileInline(admin.StackedInline):
    model = CharFile

class CharacterAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, VoiceInline, StateInline, ActiveSkillInline, ChainSkillInline, EquipSkillInline,
        EquipmentInline, BreakthroughInline, AscensionInline, SpecialRoleInLine,
         CharFileInline ]
    list_display = ('name', 'name_alphabet', 'rarity')

# Register your models here.

admin.site.register(Character, CharacterAdmin)
admin.site.register(MainAttribute)
admin.site.register(SubAttribute)
admin.site.register(CharClass)
admin.site.register(Faction)
admin.site.register(Personality)