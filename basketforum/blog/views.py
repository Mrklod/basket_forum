from django.shortcuts import render
from .models import Post
def main(request):
    return render(request,'blog/main.html')

def rules(request):
    return render(request,'blog/rules.html')

def posts(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'blog/posts.html',context=context)