from django.urls import path

from dashboard import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('buy-ico/', views.buy_ico, name='buy-ico'),
    path('manage expenses/', views.manage_expenses, name='manage expenses'),
    path('transactions/', views.transactions, name='transactions'),
    path('faq/', views.faq, name='faq'),
    path('update profile/', views.update_profile, name='update profile'),
    path('account-login-history/', views.account_login_history, name='account-login-history'),
    path('change password/', views.change_password, name='change password'),
    path('profile/', views.profile, name='profile'),

]