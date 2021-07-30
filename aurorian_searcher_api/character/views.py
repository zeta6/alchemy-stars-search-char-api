from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CharacterSerializer
from .serializers import CharacterListSerializer
from .models.character import Character
from .models.image import Image
from .models.state import State

class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()

class CharacterListView(viewsets.ModelViewSet):
    serializer_class = CharacterListSerializer
    queryset = Character.objects.all()