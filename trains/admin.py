from django.contrib import admin
from trains.models import Trains,TrainsLog,TrainsList
# Register your models here.
admin.site.register(Trains)
admin.site.register(TrainsList)
admin.site.register(TrainsLog)
