from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from biryani.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')
    

def home(request):
    return render(request,'index.html')
    #return HttpResponse("<h1>Hello This is my Home Page!")


def about(request):
    return render(request,'about.html')
    #return HttpResponse ("<h1>Hello Welcome To about page</h1>") 

def services(request):
    return render(request,'services.html')
    #return HttpResponse ("<h1>Hello Welcome To service page</h1>") 

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')
    return render(request,'contact.html')
    #return HttpResponse ("<h2>Hello Welcome To contact page</h2>") 