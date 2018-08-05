from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login_submit', views.account_view, name='account'),
    path('create_account', views.account_create, name='create'),
]
