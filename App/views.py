#Hi muathasim parambat. I really liked your work. Keep it up. And dont forget me when you become the CEO of Amazon
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Account

# Create your views here.
def home_view(request):
    return render(request, 'App/home.html')

def account_view(request):
    email = request.POST['email']
    password = request.POST['password']

    user = Account.objects.get(pk=email)
    if (user.password != password):
        return render(request, reverse('login:home'))
    else:
        return render(request, 'App/account.html', { 'user': user })

def account_create(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    user = Account(name=name, email=email, password=password)
    user.save()
    return HttpResponseRedirect(reverse('login:home'))
