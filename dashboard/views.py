from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import context

from dashboard.models import Expense, Profile
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
    obj = Expense.objects.filter(user_id=request.user)
    return render(request, 'dashboard_page/manage expenses.html', {'all_add': obj})


def transactions(request):
    return render(request, 'dashboard_page/transactions.html')


def faq(request):
    return render(request, 'dashboard_page/faq.html')


def update_profile(request):
    if request.method == 'POST':
        # try:
        User.objects.filter(id=request.user.id).update(first_name=request.POST.get('fname'),
                                                       last_name=request.POST.get('lname'))
        profile_obj = Profile.objects.get(user_id=request.user.id)
        if profile_obj:
            profile_obj.mobile = request.POST.get('mobile')
            profile_obj.city = request.POST.get('city')
            profile_obj.state = request.POST.get('state')
            profile_obj.country = request.POST.get('country')
            profile_obj.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('update-profile')
    # except:
    #     messages.error(request, "Something Went Wrong")
    #     return redirect('update-profile')
    else:
        pro_obj = Profile.objects.get(user_id=request.user.id)
        return render(request, 'dashboard_page/update-profile.html', {"user_obj": pro_obj})


def account_login_history(request):
    return render(request, 'dashboard_page/account-login-history.html')


def change_password(request):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                old_password = request.POST.get('old_password')
                new_password = request.POST.get('new_password')
                confirm_password = request.POST.get('confirm_password')
                # validation
                if not new_password == confirm_password:
                    messages.error(request, "Confirm Password Not matched with Confirm Password")
                    return redirect('change_password')
                else:
                    user = User.objects.get(email=request.user.email)
                    if user.check_password(old_password):
                        user.set_password(confirm_password)
                        user.save()
                        update_session_auth_hash(request, user)
                        messages.success(request, "Password Updated Successfully")
                        return redirect('change_password')

                    else:
                        messages.error(request, "Old Password Not match")
                        return redirect('change_password')

            else:
                return render(request, 'dashboard_page/change password.html')
        else:
            return render(request, 'dashboard_page/change password.html')
    except:
        return redirect('login')


def profile(request):
    return render(request, 'dashboard_page/profile.html')


def add_expense(request):
    if request.method == "POST":
        print('hiii')
        user1 = User.objects.get(id=request.user.id)
        # addmoney_info1 = Expense.objects.filter(user=user1).order_by('-Date')
        expense_name = request.POST.get("expense_name")
        Category = request.POST.get("Category")
        amount = request.POST.get("amount")
        mode_of_payment = request.POST.get("mode_of_payment")
        date_of_expense = request.POST.get("date_of_expense")
        add = Expense.objects.create(user=user1, expense_name=expense_name, Category=Category, amount=amount,
                                     mode_of_payment=mode_of_payment, date_of_expense=date_of_expense)
        add.save()
        # paginator = Paginator(addmoney_info1, 4)
        # page_number = request.GET.get('page')
        # page_obj = Paginator.get_page(paginator,page_number)
        # context = {
        #     'page_obj' : page_obj
        #     }
        return redirect('manage-expenses')
    else:
        return render(request, 'dashboard_page/add expense.html')


def view_expense(request):
    return render(request, 'dashboard_page/view-expense.html')


def edit_expense(request, id):
    if request.method == "POST":
        expense_obj = Expense.objects.get(pk=id,user_id=request.user.id)
        if expense_obj:
            expense_obj.Category = request.POST.get('Category')
            expense_obj.expense_name = request.POST.get('expense_name')
            expense_obj.amount = request.POST.get('amount')
            expense_obj.mode_of_payment = request.POST.get('mode_of_payment')
            expense_obj.date_of_expense = request.POST.get('date_of_expense')
            expense_obj.save()
        messages.success(request, "Expense Updated Successfully")
        return redirect('manage-expenses')
    else:
        expense = Expense.objects.get(pk=id, user_id=request.user)
        return render(request, 'dashboard_page/edit-expense.html', {'data': expense})



def logout1_request(request):
    logout(request)
    return redirect('home')


# def expense_delete(request, id):
#     Expense = User.objects.get(pk=id, id=request.user.id)
#     Expense.delete()
#     messages.success(request, 'Expense removed')
#     return redirect("manage-expenses")
    # if request.session.has_key('is_logged'):

    # return redirect("manage-expenses")

def expense_delete(request,id):
        expense_obj = Expense.objects.get(pk=id, user_id=request.user.id)
        expense_obj.delete()
        return redirect("manage-expenses")
