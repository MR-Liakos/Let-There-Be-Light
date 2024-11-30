from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return HttpResponse("And light came to be")
# Create your views here.
