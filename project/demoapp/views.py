from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'resut':obj, 'teams':obj2})
