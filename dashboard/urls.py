from django.urls import path

from dashboard import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('buy-ico/', views.buy_ico, name='buy-ico'),
    path('wallet/', views.wallet, name='wallet'),

]