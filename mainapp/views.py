from django.shortcuts import render


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
    return render(request, 'page/login.html')

def register(request):
    return render(request, 'page/register.html')

def forgot(request):
    return render(request, 'page/forgot.html')
