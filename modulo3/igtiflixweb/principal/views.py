from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    return render(request, 'principal/index.html')