from contextlib import redirect_stderr
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User


from .forms import orderForm, searchForm, UserCreateForm
from .models import Customer

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
    cust = Customer.objects.all()
    form = searchForm(request.POST or None)
    context = {
            "form": form,
            "cust": cust,
        }
    if request.method == "POST": 
        cust = Customer.objects.filter(full_name__icontains=form['full_name'].value(),
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

