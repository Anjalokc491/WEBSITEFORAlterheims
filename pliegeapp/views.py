from django.shortcuts import render
from django.http import HttpResponse



def about(request):
    return render(request,'about.html')


def appointment(request):
    return render(request,'appointment.html')

def contacts(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

# def indexappoinment(request):
#     if request.method == 'POST':


def price(request):
    return render(request,'price.html')

def service(request):
    return render(request,'service.html')

def store(request):
    return render(request,'store.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')






