from django.shortcuts import render

def base(request):
    return render(request,'blog/base.html')