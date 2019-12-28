from django.shortcuts import render
from django.http import HttpResponse
from .models import profile,profileimg,about,quto,career,metarial
# Create your views here.

def home(request):
    qoto=quto.objects.all()
    img=profileimg.objects.all()
    pro=profile.objects.all()
    meta=metarial.objects.get()
    abou=about.objects.all()
    return render(request, 'home.html',{'q':qoto,'abbb':abou,'profile':pro,'metarial':meta,'img':img})

