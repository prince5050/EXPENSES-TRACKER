from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard_page/index.html')

def buy_ico(request):
    print('hi')
    return render(request, 'dashboard_page/buy-ico.html')

def wallet(request):
    return render(request, 'dashboard_page/wallet.html')

def transactions(request):
    return render(request, 'dashboard_page/transactions.html')


def faq(request):
    return render(request, 'dashboard_page/faq.html')

def account_profile(request):
    return render(request, 'dashboard_page/account-profile.html')

def account_login_history(request):
    return render(request, 'dashboard_page/account-login-history.html')
