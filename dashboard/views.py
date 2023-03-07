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
    return render(request, 'dashboard_page/view expense.html')


def edit_expense(request):
    return render(request, 'dashboard_page/edit expense.html')


def edit_expense(request):
    if request.session.has_key('is_logged'):
        addmoney_info = Addmoney_info.objects.get(id=id)
        user_id = request.session["user_id"]
        user1 = User.objects.get(id=user_id)
        return render(request, 'home/expense_edit.html', {'addmoney_info': addmoney_info})
    return redirect("/home")


def logout1_request(request):
    logout(request)
    return redirect('home')


def add_money(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            print('hiii')
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            # addmoney_info1 = Expense.objects.filter(user=user1).order_by('-Date')
            expense_name = request.POST["expense_name"]
            Category = request.POST["Category"]
            amount = request.POST["amount"]
            mode_of_payment = request.POST["mode_of_payment"]
            date_of_expense = request.POST["date_of_expense"]
            add = Expense(user=user1, expense_name=expense_name, Category=Category, amount=amount,
                          mode_of_payment=mode_of_payment, date_of_expense=date_of_expense)
            add.save()
            # paginator = Paginator(addmoney_info1, 4)
            # page_number = request.GET.get('page')
            # page_obj = Paginator.get_page(paginator,page_number)
            # context = {
            #     'page_obj' : page_obj
            #     }
            return render(request, 'dashboard_page/manage expenses.html', context)
    return redirect('dashboard_page/index')


def add_money_update(request, id):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            add = Expense.objects.get(id=id)
            add.expense_name = request.POST["expense_name"]
            add.Category = request.POST["Category"]
            add.amount = request.POST["amount"]
            add.mode_of_payment = request.POST["mode_of_payment"]
            add.date_of_expense = request.POST["date_of_expense"]
            add.save()
            return redirect("dashboard_page/manage expenses")
    return redirect("/dashboard_page/index")
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
