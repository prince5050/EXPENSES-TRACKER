import random
import string

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.template.loader import render_to_string

from dashboard.models import Profile
from mainapp.models import Contact


# Create your views here.
def home(request):
    return render(request, 'page/index.html')



def contact(request):
    if request.method == 'POST':
        # try:
        Contact.objects.create(name=request.POST['name'].upper(), email=request.POST['email'],
                               mobile=request.POST['mobile'], subject=request.POST['subject'],
                               message=request.POST['message'])

        data = {
            'name': request.POST['name'], 'email': request.POST['email'],
            'mobile': request.POST['mobile'], 'subject': request.POST['subject'],
            'message': request.POST['message']
        }
        send_email_message('page/contact-email.html', 'Contact Mail From ' + str(request.POST['name'].upper()) + '',
                           'trishanimmalapudi2001@gmail.com', data)
        # send_mail_contact(name, email, mobile, subject, message)
        messages.success(request, "Message send successfully")
        return redirect('contact')
    # except:
    #     messages.error(request, "Something Went Wrong")
    #     return redirect('home')
    else:
        return render(request, 'page/contact.html')


def about(request):
    return render(request, 'page/about.html')


def services(request):
    return render(request, 'page/services.html')


def exchange(request):
    return render(request, 'page/exchange.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('psw')
        try:
            user_obj = User.objects.get(username=email)
            # print(user_obj.first_name)
            if user_obj.check_password(password):
                login(request, user_obj)
                return redirect('dashboard')
            else:
                messages.success(request, 'Password is Incorrect')
                return redirect('login')
        except:
            messages.error(request, 'Email is not matched')
            return redirect('login')

    else:
        return render(request, 'page/login.html')


def register(request):
    if request.method == 'POST':
        #     first_name = request.POST.get('fname')
        #     last_name = request.POST.get('lname')
        #     email = request.POST.get('email')
        #     password = request.POST.get('password')
        if User.objects.filter(email=request.POST.get('email')).first():
            messages.error(request, 'Email is already taken. Try with another')
            return render(request, 'page/register.html')
        else:
            user_obj = User.objects.create_user(username=request.POST.get('email'),
                                                first_name=request.POST.get('first_name'),
                                                last_name=request.POST.get('last_name'),
                                                email=request.POST.get('email'), password=request.POST.get('password'))
            user_obj.save()
            profile_obj = Profile.objects.create(user_id=user_obj.id, mobile=request.POST.get('mobile'))
            profile_obj.save()
            messages.success(request, 'Registration has successfully completed')
            return render(request, 'page/register.html')

    else:
        return render(request, 'page/register.html')


def forgot(request):
    # try:
        if request.method == "POST":
            user_obj = User.objects.filter(username=request.POST.get('email').lower())
            if user_obj:
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                user = User.objects.get(username=request.POST.get('email').lower())
                user.set_password(password)
                user.save()
                data = {
                    'password': password,
                    'first_name': user.first_name,
                    'last_name': user.last_name,

                }
                send_email_message('page/forgot_email.html', 'Reset Password | EXPENSES TRACKER',
                                   request.POST.get('email'), data)
                messages.success(request, 'System Generated password has been sent on your registered E-mail')
                return redirect('login')

            else:
                messages.error(request, 'Invalid E-mail Id,Try again')
                return redirect('forgot')

        else:
            return render(request, 'page/forgot.html')
    # except:
    #     return redirect('login')


def send_email_message(email_template, subject, to_email, data):
    html_message = render_to_string(email_template, data)
    mail_subject = subject
    message = html_message
    to_email = [to_email]
    # 'sales@amtz.in', 'finance@amtz.in'
    email = EmailMultiAlternatives(
        mail_subject,
        "hello",  # necessary to pass some message here
        settings.EMAIL_HOST_USER, to_email)
    email.attach_alternative(message, "text/html")
    email.send(fail_silently=False)

