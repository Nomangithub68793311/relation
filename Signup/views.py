from django.shortcuts import render
from django.http import HttpResponse
from Signup.models import User
from rest_framework.response import Response
from django.http.response import JsonResponse 
from rest_framework.decorators import api_view
from Signup.serializers import Adddataserializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from django.contrib.auth.hashers import make_password,check_password
from django.forms.models import model_to_dict

import json
@csrf_exempt
def signUppost(request):
        if (request.method=='POST'):
            data = JSONParser().parse(request)
            # user=User.objects.get(email=data['email'])
            # serializer = Adddataserializer(data=user)
            # print(user)
            data['password']=make_password(data['password'])
            serializer = Adddataserializer(data=data)
            if serializer.is_valid():
                        serializer.save()
                        print(serializer.data)
                        return JsonResponse({
                            "email":serializer.data['email']        


                        })
            return JsonResponse(serializer.errors, status=400)   
                

            
                            
            # return JsonResponse({"response":"Email exists"})
        # data_ser=Adddataserializer(user)
        # if data_ser.is_valid():
        #     data_ser.save()
        #     # print(data_ser.data)
        #     return JsonResponse(data_ser.data,safe=False)
        # return JsonResponse("failed")               
    
@csrf_exempt      
def login(request):
    if (request.method=='POST'):
            data = JSONParser().parse(request)
            user=User.objects.filter(email=data['email']).first()
            print(user.email)
            if(user):
                    matched=check_password(data['password'],user.password)
                    if(matched):
                        return  JsonResponse({
                        "success":'token'
                    })
                    return  JsonResponse({
                        "success":'password doesnt match'
                
                    })
            return  JsonResponse({
                        "success":'email not match'
                    })   
                    
           

            
def logout(request):
    return HttpResponse('from logout')
def sendCode(request):
     if (request.method=='GET'):
        dataall=User.objects.all()
        data_ser=Adddataserializer(dataall,many=True)
 
        return JsonResponse(data_ser.data,safe=False) 
@csrf_exempt        
def update(request,pk):
     if (request.method=='PUT'):
        data = JSONParser().parse(request)
        dataall=User.objects.filter(id=pk).update(name = data['name'],age=data['age'])
        # dataall['name']=data['name']
        # dataall['age']=data['age']
        print(dataall)
        serializer = Adddataserializer(data=dataall)
        if serializer.is_valid():
                        serializer.save()
                        print(serializer.data)
                        return JsonResponse({
                            "email":serializer.data['email']        


                        })
        return JsonResponse(serializer.errors, status=400)
                                 