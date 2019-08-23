from django.shortcuts import render
from django.http import HttpResponse
from trains.forms import AddTrains,ChooseTrainDate
from trains.models import Trains,TrainsLog
from django.http import HttpResponseRedirect

# Create your views here.

def FormAddTrains(request):
    if request.method == 'POST':
        form = AddTrains(request.POST)
        if form.is_valid():
            user1 = form.save()
            print('Поздравляем Вы записаны',user1)
            return HttpResponseRedirect('/')
    else:
        form = AddTrains()
    return render(request,'add.html',{'form' :form})

def FormChoicesDate(request):
    if request.method == 'POST':
        form = ChooseTrainDate(request.POST)
        if form.is_valid():
            date1 = form.save()
            print('Дата выбрана')
            return HttpResponseRedirect('/addv2/')
    else:
        form = ChooseTrainDate()
    return  render(request,'add.html',{'form': form})


def StaticTrains(request):
    ppp = TrainsLog.objects.filter(istrain=True)
    return HttpResponse("Hello, world. You're at the poll index.")



