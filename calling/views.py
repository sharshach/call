from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def homepage(req,mobileNum):
    os.system("termux-telephony-call "+str(mobileNum))
    return HttpResponse("<h1>hello2</h1>")