from django.shortcuts import render

# Create your views here.
from media_app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}

    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            UFO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            UFO.set_password(password)
            UFO.save()

            PFO=PFD.save(commit=False)
            PFO.profile_user=UFO
            PFO.save()

        return HttpResponse('registration is succeffull')


    return render(request,'registration.html',d)
def user_login(request):
    if request.method=='POST':
        username=request.post['un']
        password=request.post['pn']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
           login(request.user)
           request.session['username'] = username
           return HttpResponseRedirect(reverse('home'))
        
        
    return render(request,'login.html')
    
