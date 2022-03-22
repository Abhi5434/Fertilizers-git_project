from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request ,'register.html' ,{'form':form,'msg':"Registered Successfully"})
        else:
            form = UserCreationForm()
        return render(request, "register.html", {'form': form})
