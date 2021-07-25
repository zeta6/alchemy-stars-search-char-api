from rest_framework import serializers
from .models.character import Character
from .models.image import Image
from .models.main_attr import MainAttribute
from .models.sub_attr import SubAttribute
from .models.char_class import CharClass
from .models.faction import Faction
from .models.personality import Personality
from .models.state import State


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

class CharacterSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    main_attribute = MainAttributeSerializer()
    sub_attribute = SubAttributeSerializer()
    char_class = CharClassSerializer()
    faction = FactionSerializer()
    personality = PersonalitySerializer()
    state = StateSerializer()

    class Meta:
        model = Character
        fields = ('id', 'name', 'name_alphabet', 'state', 'image', 'rarity','main_attribute', 'sub_attribute', 'char_class', 'faction', 'personality', 'state')
