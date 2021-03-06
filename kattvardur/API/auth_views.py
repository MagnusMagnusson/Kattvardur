from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.http.response import JsonResponse
from People.serializers import PersonSerializer
import requests
import json
from django.conf import settings

def Login(request): 
    print(request.user)
    if request.method != "POST":
        return JsonResponse({"msg":"Method Not Allowed"}, status = 405)
    body = json.loads(request.body)
    if 'user' not in body or 'password' not in body:
        return JsonResponse({"error":"Authentication Failed"},  status=401)
    u = body['user']
    p = body['password']
    user = authenticate(username = u, password = p)
    if user is not None:
        if user.person is not None:
            login(request, user)
            return JsonResponse(PersonSerializer(user.person).data, status = 200)
        return JsonResponse({"msg":"authenticated"},status=200)
    else:
        return JsonResponse({"error":"Authentication Failed"},  status=401)

def Logout(request):
    if request.user.is_authenticated():
        logout(request)
        return JsonResponse({}, status=200)
    else:
        return JsonResponse({}, status = 401)


def ValidateGoogleToken(token_id):
    Gurl = 'https://oauth2.googleapis.com/tokeninfo?'
    response = requests.get(
        Gurl,
        params = {'id_token': token_id}
    )
    if not response.ok:
        raise ValidationError("Token validation failed")

    response = response.json()
    aud = response['aud']
    if aud != settings.KATTVARDUR_GOOGLE_CLIENT_ID:
       raise ValidationError('Audience validation failed')
    return True

def OauthLogin(request):
    if request.method != "POST":
        return JsonResponse({"msg":"Method Not Allowed"}, status = 405)
    token_id = request.META['HTTP_AUTHORIZATION']
    try:
        if ValidateGoogleToken(token_id):
            body = json.loads(request.body)
            email = body['email']
            print(email)
            try:
                user = User.objects.get(email__iexact=email)
                login(request, user)
                userDict = {
                    "first_name" : user.first_name,
                    "last_name" : user.last_name,
                    "email" : user.email,
                }
                return JsonResponse({"user": userDict}, status=200)
            except User.DoesNotExist:
                return JsonResponse({"error":"Authentication Failed"},  status=401)        
    except ValidationError:
            return JsonResponse({"error":"Validation Failed"},  status=401)  
    

