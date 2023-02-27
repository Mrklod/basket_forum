from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import Post
from .forms import PostForm
def main(request):
    return render(request,'blog/main.html')

def rules(request):
    return render(request,'blog/rules.html')

def posts(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'blog/posts.html',context=context)

def single_post(request,post_id):
    post = Post.objects.filter(pk=post_id)
    context = {'post':post}
    return render(request,'blog/single_post.html',context=context)

def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts'))
    context = {'form':form}
    return render(request,'blog/add_post.html',context=context)