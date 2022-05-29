from contextlib import redirect_stderr
from urllib.robotparser import RequestRate
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User


from .forms import orderForm, searchForm, UserCreateForm
from .models import Customer, Gambar, Gambar2, Gambar3

# Create your views here.
def home(request):
    return render(request, 'index.html')


def register(request):  
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserCreateForm()

    return render(request, 'register.html', {'form':form})


def list(request):
    cust = Customer.objects.filter(user_name = request.user)
    form = searchForm(request.POST or None)
    context = {
            "form": form,
            "cust": cust,
        }
    if request.method == "POST": 
        cust = Customer.objects.filter(description__icontains=form['description'].value(),
                                            )
        context = {
            "form": form,
            "cust": cust,
        }

    return render(request, 'list.html',context)


def order(request):
    if request.method == "POST":
        form = orderForm(request.POST)
        if form.is_valid():
            pesan = form.save(commit= False)
            pesan.user_name = request.user
            pesan.save()
            return redirect('home')
    else:
        form = orderForm()

    return render(request, 'order.html', {'form': form})

def gambar(request, gambar_id):
    gambar = Gambar.objects.get(pk=gambar_id)
    if gambar is not None:
        return render(request, 'index.html', {'gambar':gambar})
    else:
        raise Http404('Gambarnya gaada')

def home2(request):
    gambar = Gambar.objects.all()
    gambar2 = Gambar2.objects.all()
    gambar3 = Gambar3.objects.all()
    
    return render(request, 'index.html', {'gambar':gambar, 'gambar2':gambar2, 'gambar3':gambar3})
    
