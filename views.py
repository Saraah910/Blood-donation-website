from tkinter import Variable
from django.shortcuts import render,HttpResponse
from matplotlib.style import context
from home.models import Contact
from datetime import datetime

def index(request):
    context = {
        'variable' : "Varible 1 is sent"
    }
    return render(request,'index.html')
    # return HttpResponse("This is homepage")
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name = name,email = email,subject = subject,message = message,date = datetime.today())
        contact.save()
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')