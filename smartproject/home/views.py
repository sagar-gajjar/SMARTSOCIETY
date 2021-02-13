from django.shortcuts import render
from chairman.views import *
from society_member.views import *
from watchman.views import *

# Create your views here.

def home(request):
    return render(request,"home/login.html")