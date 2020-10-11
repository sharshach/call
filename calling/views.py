from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os
import json

def call(req,mobileNum):
    os.system("termux-telephony-call "+str(mobileNum))
    return HttpResponse("<h1>hello2</h1>")
def contacts(req):
    try:
        contactsList=open('data.json').read()
    except:
        print("rename data_sample.json to data.json")
        contactsList=open('data_sample.json').read()
    context = {
        'contactsList': json.loads(contactsList),
    }
    return render(req, 'calling/index.html', context)