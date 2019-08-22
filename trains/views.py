from django.shortcuts import render
from django.http import HttpResponse
from trains.forms import AddTrains,ChooseTrainDate
from trains.models import Trains
from django.http import HttpResponseRedirect

# Create your views here.

def FormAddTrains(request):
    if request.method == 'POST':
        form = AddTrains(request.POST)
        if form.is_valid():
            user1 = form.save()
            print('Поздравляем Вы записаны',user1)
            return HttpResponseRedirect('')
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
    ppp = Trains.objects.filter(date__month=8)
    print(ppp)
    return HttpResponse(ppp, "Hello, world. You're at the poll index.")



