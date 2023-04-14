from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic Inserted Successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['nm']
        url=request.POST['ur']
        email=request.POST['em']
        TO=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage Inserted Successfully')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    LWO=Webpage.objects.all()
    d={'webpages':LWO}

    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['ar']
        date=request.POST['dt']
        WO=Webpage.objects.get(name=name)
        AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('Accessrecord  Inserted Successfully')
    return render(request,'insert_access.html',d)


