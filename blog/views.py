from django.shortcuts import render
from django.http import HttpResponse
import json as json
# Create your views here.

def index(request):
    local = dict()
    local['hello'] = "world"
    return HttpResponse(json.dumps(local))
