from django.contrib import admin
from trains.models import Trains,TrainsLog,TrainsList,Trener
# Register your models here.
admin.site.register(Trains)
admin.site.register(TrainsList)
admin.site.register(TrainsLog)
admin.site.register(Trener)
