from rest_framework import serializers
from .models.character import Character
from .models.image import Image
from .models.main_attr import MainAttribute
from .models.sub_attr import SubAttribute
from .models.char_class import CharClass
from .models.faction import Faction
from .models.personality import Personality
from .models.state import State
from .models.chain_skill import ChainSkill
from .models.active_skill import ActiveSkill
from .models.equip_skill import EquipSkill
from .models.equipment import Equipment
from .models.breakthrough import Breakthrough
from .models.ascension import Ascension
from .models.char_file import CharFile
from .models.voice import Voice


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('ascension_0', 'ascension_3',)

class MainAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAttribute
        fields = ('name', 'icon',)

class SubAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAttribute
        fields = ('name', 'icon',)

class CharClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharClass
        fields = ('name', 'icon',)

class FactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faction
        fields = ('name', 'icon', 'small_gift', 'big_gift')

class PersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Personality
        fields = ('name', 'small_gift', 'big_gift')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('attack', 'defence', 'hit_point')

class ChainSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainSkill
        fields = ('name', 'icon', 'lv1_tiles','lv1_text', 'lv2_tiles', 'lv2_text', 'lv3_tiles', 'lv3_text')

class ActiveSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveSkill
        fields = ('name', 'cooltime', 'preemptive','icon', 'text', 'brth_skill_1_br', 'brth_skill_2_br',
         'asc0_brth_skill_1_cooltime', 'asc0_brth_skill_1_preemptive', 'asc0_brth_skill_1_text',
         'asc0_brth_skill_2_cooltime', 'asc0_brth_skill_2_preemptive', 'asc0_brth_skill_2_text',
         'asc2_brth_skill_0_cooltime', 'asc2_brth_skill_0_preemptive', 'asc2_brth_skill_0_text',
         'asc2_brth_skill_1_cooltime', 'asc2_brth_skill_1_preemptive', 'asc2_brth_skill_1_text',
         'asc2_brth_skill_2_cooltime', 'asc2_brth_skill_2_preemptive', 'asc2_brth_skill_2_text',
         'asc3_brth_skill_0_cooltime', 'asc3_brth_skill_0_preemptive', 'asc3_brth_skill_0_text',
         'asc3_brth_skill_1_cooltime', 'asc3_brth_skill_1_preemptive', 'asc3_brth_skill_1_text',
         'asc3_brth_skill_2_cooltime', 'asc3_brth_skill_2_preemptive', 'asc3_brth_skill_2_text')

class EquipSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipSkill
        fields = ('name', 'icon', 'lv1_text', 'lv3_text', 'lv6_text', 'lv10_text', 'asc2_enhance',
            'asc2_lv1_text', 'asc2_lv3_text', 'asc2_lv6_text', 'asc2_lv10_text', 'asc3_enhance',
            'asc3_lv1_text', 'asc3_lv3_text', 'asc3_lv6_text', 'asc3_lv10_text'    
            )
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('name', 'image', 'lv1_text', 'lv3_text', 'lv6_text', 'lv10_text', 'lv1_state_text',
            'lv2_state_text', 'lv4_state_text', 'lv5_state_text', 'lv7_state_text', 'lv8_state_text',
            'lv9_state_text')

from .models.breakthrough import Breakthrough
from .models.ascension import Ascension
from .models.char_file import CharFile
from .models.voice import Voice

class BreakthroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breakthrough
        fields = ('count_1', 'count_2', 'count_3', 'count_4', 'count_5', 'count_6')

class AscensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ascension
        fields = ('lv1', 'lv2', 'lv3')

class CharFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharFile
        fields = ('name', 'nickname', 'gender', 'height', 'birthday', 'birthplace',
        'element', 'affilition', 'fighting_style')

class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = ('name')

class CharacterSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)
    main_attribute = MainAttributeSerializer(read_only=True)
    sub_attribute = SubAttributeSerializer(read_only=True)
    char_class = CharClassSerializer(read_only=True)
    faction = FactionSerializer(read_only=True)
    personality = PersonalitySerializer(read_only=True)
    state = StateSerializer(read_only=True)
    chain_skill = ChainSkillSerializer(read_only=True)
    active_skill = ActiveSkillSerializer(read_only=True)
    equip_skill = EquipSkillSerializer(read_only=True)
    equipment = EquipmentSerializer(read_only=True)
    breakthrough = BreakthroughSerializer(read_only=True)
    ascension = AscensionSerializer(read_only=True)
    charFile = CharFileSerializer(read_only=True)
    voice = VoiceSerializer(read_only=True)

    class Meta:
        model = Character
        fields = ('id', 'name', 'name_alphabet', 'state', 'image', 'rarity','main_attribute',
         'sub_attribute', 'char_class', 'faction', 'personality', 'state', 'chain_skill', 'active_skill',
         'equip_skill', 'equipment', 'breakthrough', 'ascension', 'charFile', 'voice'
         )
