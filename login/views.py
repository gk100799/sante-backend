from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from login.models import User
from login.serializers import LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

@api_view(['POST'])
def user_login(request):
    #if request.method == "POST":
    serializer_class = LoginSerializer
    username = request.data['username']
    password = request.data['password']
    try:
        user = User.objects.get(username = username, password = password)
    except:
        return Response({"message":"Invalid Username or Password"},status=status.HTTP_401_UNAUTHORIZED)
    return Response({"message":"successfully logged in!"}, status=status.HTTP_202_ACCEPTED)


# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.contrib.auth import authenticate as userAuthenticate, login as auth_login, logout as auth_logout
# from django.utils.datastructures import MultiValueDictKeyError
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import update_last_login
# from .models import ScoreUser
# import logging
# from django.conf import settings
# import re
# import json
# from django.views.decorators.csrf import csrf_exempt

# logger = logging.getLogger('AM')


# @csrf_exempt
# def authenticate(request):
#     """
#     ---------------------------------------------------------------------------
#     Authenticate the user based on the username and
#     password.
#     ---------------------------------------------------------------------------
#     :param request: HTTP Request Parameter with POST Data
#     :return: HTTP Render Response
#     """
#     """
#     TODO: Handle the Loggin and Tracing
#     """
#     # Get the Username and Password from the HTTP Request
#     #
#     try:
#         jsonData = json.loads(request.body.decode('utf-8'))
#         username = jsonData['Username']
#         password = jsonData['Password']

#         logger.info("Login Requested")

#     except MultiValueDictKeyError:
#         logger.error('Username or Password missing in the HTTP Request')
#         # if the Error Message defined share the message
#         return JsonResponse(status=500, safe=False)

#     # Authenticate the  user based on the username and password
#     #
#     user = userAuthenticate(username=username, password=password)
    
#     if user:
#         logger.info('%s User Authenticated', username)
#         auth_login(request, user)
#         responseData = {
#             'isAuthenticated': 'true',
#             'firstLogin': True,
#             'url': '/dashboard/home'
#         }
#         request.session['userId'] = user.email
#         return JsonResponse(responseData, status=200)        
#     else:
        
# logger.error('Incorrect login info for User %s', username)
#         responseData = {
#             'isAuthenticated': 'false',
#             'uuid': '',
#             'invalidCredentials':'True',
#         }
#         return JsonResponse(responseData, status=401)



