from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard_page/index.html')

def buy_ico(request):
    print('hi')
    return render(request, 'dashboard_page/buy-ico.html')

def wallet(request):
    return render(request, 'dashboard_page/wallet.html')
