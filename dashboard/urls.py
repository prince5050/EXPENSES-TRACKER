from django.urls import path

from dashboard import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('buy-ico/', views.buy_ico, name='buy-ico'),
    path('wallet/', views.wallet, name='wallet'),
    path('transactions/', views.transactions, name='transactions'),
    path('faq/', views.faq, name='faq'),
    path('account-profile/', views.account_profile, name='account-profile'),
    path('account-login-history/', views.account_login_history, name='account-login-history'),

]