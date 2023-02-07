from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'page/index.html')

def contact(request):
    return render(request, 'page/contact.html')


def about(request):
    return render(request, 'page/about.html')


def services(request):
    return render(request, 'page/services.html')

def exchange(request):
    return render(request, 'page/exchange.html')

def login(request):
    if request.method == 'GET':
        Next = request.GET.get('next')
        cache.set('next', Next)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return render(request, 'page/login.html')

def register(request):
    if request.method == 'POST':
    #     first_name = request.POST.get('fname')
    #     last_name = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
        if User.objects.filter(email=request.POST.get('email')).first() :
            messages.error(request, 'Email is already taken. Try with another')
            return render(request, 'page/register.html')
        else:
            user_obj = User.objects.create_user(username=request.POST.get('email'), first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'),
                                                email=request.POST.get('email'), password=request.POST.get('password'))
            user_obj.save()
            messages.info(request, 'Registration has successfully completed')
            return render(request, 'page/register.html')

    else:
        return render(request, 'page/register.html')




def forgot(request):
    return render(request, 'page/forgot.html')





