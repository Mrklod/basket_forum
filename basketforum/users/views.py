from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from .forms import UserLoginForm,UserRestrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm
    context = {'form':form}
    return render(request,'users/login.html',context=context)
def register(request):
    if request.method == 'POST':
        form = UserRestrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRestrationForm()
    context = {'form':form}
    return render(request,'users/register.html',context=context)
