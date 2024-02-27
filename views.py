from django.shortcuts import render
from .serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
class register(APIView):

    def post(self, request, format=None):
    # Your method implementation goes here
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token, created = Token.objects.get_or_create(user=account)
            data['token'] = token.key if created else Token.objects.get(user=account).key

        else:
            data=serializer.errors
        return Response(data)


