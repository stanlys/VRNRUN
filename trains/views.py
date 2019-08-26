from django.shortcuts import render
from django.http import HttpResponse
from trains.forms import AddTrains,ChooseTrainDate
from trains.models import Trains,TrainsLog,TrainsList,Trener
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
    if request.method == 'GET':
        form = ChooseTrainDate(request.GET)
        if form.is_valid():
            print(TrainsList.objects.filter(trainsday__month=form.cleaned_data['date']))
            date1 = form.save()
            return HttpResponseRedirect('/stat_step2/')
    else:
        form = ChooseTrainDate()
    return  render(request,'add.html',{'form': form})


def StaticTrains(request):
    TrainsList.objects.filter(id=1).delete()
    return HttpResponse( "Hello, world. {} You're at the poll index.".format(TrainsList.objects.all().count()))


