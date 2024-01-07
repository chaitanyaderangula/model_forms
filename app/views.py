from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid:
            TFDO.save()
            return HttpResponse('insert_topic is Done')    
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WTFO=Webpageform()
    d={'WTFO':WTFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_webpage is Done')
    return render(request,'insert_webpage.html',d)

def AccessRecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=="POST":
        EADO=AccessRecordForm(request.POST)
        if EADO.is_valid:
            EADO.save()
            return HttpResponse('AccessRecord is Done')
        else:
            return HttpResponse('invalid data')
    return render(request,'AccessRecord.html',d)
    