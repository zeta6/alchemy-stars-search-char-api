from rest_framework import serializers

from .models import RecruitBanner

class RecruitBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitBanner
        fields = ('id', 'name', 'image', 'char_id_not_included', 'rarity_5_pickup', 'rarity_6_pickup')