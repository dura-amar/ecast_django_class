from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from authentication.forms import RegistrationForm, loginForm

# Create your views here.
def registrationForm(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_destinations')
    return render(request,'register.html',{'form':form})

def login_view(request):
    form=loginForm()
    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('all_destinations')
            else:
                return HttpResponse('this is wrong details')
    return render(request,'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('all_destinations')


