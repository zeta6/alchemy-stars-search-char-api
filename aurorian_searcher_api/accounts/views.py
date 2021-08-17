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
from google.auth import jwt

def google_login(request):
    token = request.META['HTTP_AUTHORIZATION']
    userjson = jwt.decode(token, verify=None)
    try:
        user = User.objects.get(email=userjson["email"])
        if user.provider != "google" or user.sub != userjson["sub"] or user.azp != userjson["azp"]:
            return JsonResponse({'err_msg': 'login error'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.at_hash = userjson["at_hash"]
            user.sub = userjson["sub"]
            user.azp = userjson["azp"] 
            user.save()
            userDict = { "email" : user.email, "fav_char" : user.fav_char, "owned_char" : user.owned_char }
            return JsonResponse(userDict)

    except User.DoesNotExist:
        User.objects.create(email=userjson["email"], provider="google", sub=userjson["sub"], azp=userjson["azp"], fav_char="[]", owned_char="[]")
        user = User.objects.get(email=userjson["email"])
        userDict = { "email" : user.email, "provider" : user.provider,  "fav_char" : user.fav_char, "owned_char" : user.owned_char }
        return JsonResponse(userDict)


def google_withdrawal(request):
    token = request.META['HTTP_AUTHORIZATION']
    userjson = jwt.decode(token, verify=None)
    user = User.objects.get(email=userjson["email"])
    if user.sub == userjson["sub"] and user.azp == userjson["azp"]:
        user.delete()
        return JsonResponse({ "del" : "success" })
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)    

@method_decorator(csrf_exempt, name="dispatch")
def fav_char_update(request):
    token = request.META['HTTP_AUTHORIZATION']
    userjson = jwt.decode(token, verify=None)
    user = User.objects.get(email=userjson["email"])
    if user.sub == userjson["sub"] and user.azp == userjson["azp"]:
        user.fav_char = (json.loads(request.body)["fav_char"])
        user.save()
        resjson = { "fav_char" : user.fav_char }
        return JsonResponse(resjson)
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)

def fav_char(request):
    token = request.META['HTTP_AUTHORIZATION']
    userjson = jwt.decode(token, verify=None)
    user = User.objects.get(email=userjson["email"])
    if user.sub == userjson["sub"] and user.azp == userjson["azp"]:
        resjson = { "fav_char" : user.fav_char }
        return JsonResponse(resjson)
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
def owned_char_update(request):
    token = request.META['HTTP_AUTHORIZATION']
    userjson = jwt.decode(token, verify=None)
    user = User.objects.get(email=userjson["email"])
    if user.sub == userjson["sub"] and user.azp == userjson["azp"]:
        user.owned_char = (json.loads(request.body)["owned_char"])
        user.save()
        resjson = { "owned_char" : user.owned_char }
        return JsonResponse(resjson)
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)


def owned_char(request):
    token = request.META['HTTP_AUTHORIZATION']
    userjson = jwt.decode(token, verify=None)
    user = User.objects.get(email=userjson["email"])
    if user.sub == userjson["sub"] and user.azp == userjson["azp"]:
        resjson = { "owned_char" : user.owned_char }
        return JsonResponse(resjson)
    else:
        return JsonResponse({'err_msg': 'access token error'}, status=status.HTTP_400_BAD_REQUEST)