from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("欢迎来到 Django 最小化项目！")