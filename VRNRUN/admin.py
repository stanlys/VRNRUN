from django.contrib import admin
from user.models import User
from trains.models import Trains

admin.site.register(User)
admin.site.register(Trains)