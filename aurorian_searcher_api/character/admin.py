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

class ImageInline(admin.TabularInline):
    model = Image

class StateInline(admin.TabularInline):
    model = State

class ChainSkillInline(admin.StackedInline):
    model = ChainSkill

class CharacterAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, StateInline, ChainSkillInline    ]
    list_display = ('name', 'name_alphabet', 'rarity')

# Register your models here.

admin.site.register(Character, CharacterAdmin)
admin.site.register(MainAttribute)
admin.site.register(SubAttribute)
admin.site.register(CharClass)
admin.site.register(Faction)
admin.site.register(Personality)