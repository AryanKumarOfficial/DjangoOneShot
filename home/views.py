from django.shortcuts import render,HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact

def index(request):
    context ={
        "title":"Home"
    }
    # return HttpResponse('This is homepage.')
    messages.success(request,"This is the test message")
    return render(request, 'index.html',context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")


    return render(request, 'contact.html')