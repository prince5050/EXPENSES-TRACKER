from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import context

from dashboard.models import Expense
from expensestracker import settings


# Create your views here.
@login_required()
def dashboard(request):
    obj = Expense.objects.filter(user_id=request.user)
    amt = []
    expenses_type = []
    for i in obj:
        amt.append(i.amount)
        expenses_type.append(i.Category)
    return render(request, 'dashboard_page/index.html', {'amt': amt, 'expenses_type': expenses_type})
#
# def buy_ico(request):
#     print('hi')
#     return render(request, 'dashboard_page/buy-ico.html')

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



# def add_expense(request):
#     if request.method == 'POST':
#         if User.objects.filter(Expense_name=request.POST.get('expense_name')).first():
#             messages.error(request, 'Expense name is already exists')
#             return render(request, 'dashboard_page/add expense.html')
#         else:
#             user_obj = User.objects.add_expense(Expense_name=request.POST.get('expense name'),
#                                                 Category=request.POST.get('category'),
#                                                 Expense_type=request.POST.get('expense type'),
#                                                 amount=request.POST.get('amount'),
#                                                 date_of_expense=request.POST.get('date of expense'), mode_of_payment=request.POST.get('mode of payment'))
#             user_obj.save()
#             messages.success(request, 'Expense added successfully')
#             return render(request, 'dashboard_page/add expense.html')
#     else:
#         return render(request,'dashboard_page/add expense.html')


        # try:
        #     expense_name = request.post['expense_name']
        #     if not expense_name:
        #         messages.error(request,'Expense name is required')
        #         return render(request, 'dashboard_page/add_expense.html',context)
        #     Category = request.POST['category']
         #    expense_type = request.post['expense_type']
        #     if not expense_type:
        #         messages.error(request,'Expense type is required')
        #         return render(request, 'dashboard_page/add_expense.html',context)

        #
        #
        #
        # except:
        #     return redirect('dashboard_page/manage expenses.html')





