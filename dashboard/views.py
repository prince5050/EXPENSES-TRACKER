from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard_page/index.html')

def buy_ico(request):
    print('hi')
    return render(request, 'dashboard_page/buy-ico.html')

def manage_expenses(request):
    return render(request, 'dashboard_page/manage expenses.html')

def transactions(request):
    return render(request, 'dashboard_page/transactions.html')


def faq(request):
    return render(request, 'dashboard_page/faq.html')

def update_profile(request):
    return render(request, 'dashboard_page/update profile.html')

def account_login_history(request):
    return render(request, 'dashboard_page/account-login-history.html')

def change_password(request):
    return render(request, 'dashboard_page/change password.html')

def profile(request):
    return render(request, 'dashboard_page/profile.html')

def add_expense(request):
    return render(request, 'dashboard_page/add expense.html')

def view_expense(request):
    return render(request, 'dashboard_page/view expense.html')
def edit_expense(request):
    return render(request, 'dashboard_page/edit expense.html')






