from django.shortcuts import render
from django.http import HttpResponse
import json as json
# Create your views here.

def index(request):
    local = dict()
    local['hello'] = "world"
    return HttpResponse(json.dumps(local))

def welcome(request):
    return HttpResponse("Welcome to my blog site!")

def poem(request):
    return render(request, "index.html", {'writer': 'By Django HttpResponse'})
