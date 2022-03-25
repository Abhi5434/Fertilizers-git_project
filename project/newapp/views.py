from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .import models
# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')
        else:
            form = UserCreationForm()
    else:
        return render(request, "register.html", {'form': UserCreationForm})




def Login(request):
    return render(request,'login.html')