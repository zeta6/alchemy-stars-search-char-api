from django.shortcuts import redirect
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse
from json.decoder import JSONDecodeError
from rest_framework import status
from rest_framework.response import Response
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name="dispatch")
def google_login(request):
    userjson = json.loads(request.body)
    try:
        user = User.objects.get(email=userjson["email"])
        if user.provider != "google" or user.provider_id != userjson["id"]:
            return JsonResponse({'err_msg': 'provider or provider ID error'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.access_token = userjson["access_token"]
            user.save()
            userDict = { "email" : user.email, "provider" : user.provider, "id" : user.provider_id, "access_token" : user.access_token, "fav_char" : user.fav_char }
            return JsonResponse(userDict)

    except User.DoesNotExist:
        User.objects.create(email=userjson["email"], provider=userjson["provider"], provider_id=userjson["id"], access_token=userjson["access_token"])
        user = User.objects.get(email=userjson["email"])
        userDict = { "email" : user.email, "provider" : user.provider, "id" : user.provider_id, "access_token" : user.access_token, "fav_char" : user.fav_char }
        return JsonResponse(userDict)

@method_decorator(csrf_exempt, name="dispatch")
def fav_char_update(request):
    userjson = json.loads(request.body)
    user = User.objects.get(email=userjson["email"])
    if user.access_token == userjson["access_token"]:
        user.fav_char = userjson["fav_char"]
        user.save()
        resjson = { "fav_char" : user.fav_char }
        return JsonResponse(resjson)
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name="dispatch")
def fav_char(request):
    userjson = json.loads(request.body)
    user = User.objects.get(email=userjson["email"])
    if user.access_token == userjson["access_token"]:
        resjson = { "fav_char" : user.fav_char }
        return JsonResponse(resjson)
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)