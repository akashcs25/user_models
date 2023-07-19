from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def display(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessRecordForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST' and request.FILES:
        tfod=TopicForm(request.POST)
        wfod=WebpageForm(request.POST,request.FILES)
        afod=AccessRecordForm(request.POST)
        if tfod.is_valid() and wfod.is_valid() and afod.is_valid():
            ntfod= tfod.save(commit=False)
            ntfod.save()
            nwfod = wfod.save(commit=False)
            nwfod.topic_name=ntfod
            nwfod.save()
            nafod=afod.save(commit=False)
            nafod.name=nwfod
            nafod.save()
            return HttpResponse('successfulllllll!!!!!!!!!!!')

    return render(request,'display.html',d)