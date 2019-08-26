from django.http import HttpResponse
from trains.models import Trener
from django.shortcuts import render
def index(request):
    TEMPLATE_PREVIEW = "index.html"
    form = Trener.objects.filter(isshow=True)
    return render(request, TEMPLATE_PREVIEW,{'form':form,'count': 12//form.count(),'LOGIN_URL': '/accounts/login/'})