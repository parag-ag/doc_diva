from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Music')

def albums(request):
    return HttpResponse('Hello Albums')
