from django.shortcuts import render
from django.http import HttpResponse
import json as json
from . import models
# Create your views here.

def index(request):
    local = dict()
    local['hello'] = "world"
    return HttpResponse(json.dumps(local))

def welcome(request):
    return HttpResponse("Welcome to my blog site!")

def poem(request):
    return render(request, "blog/index.html", {'writer': 'By Django HttpResponse'})

def article(request):
    return HttpResponse(models.Article.objects.get(pk=1))

def message(request):
    return HttpResponse(models.Message.objects.get(pk=1))
