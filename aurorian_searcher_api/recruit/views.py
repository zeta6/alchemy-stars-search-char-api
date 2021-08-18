from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecruitBannerSerializer
from .models import RecruitBanner

class RecruitBannerView(viewsets.ModelViewSet):
    serializer_class = RecruitBannerSerializer
    queryset = RecruitBanner.objects.all()