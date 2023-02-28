from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from users.models import Users
def main(request):
    return render(request,'blog/main.html')

def rules(request):
    return render(request,'blog/rules.html')
@login_required
def posts(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request,'blog/posts.html',context=context)
@login_required
def single_post(request,post_id):
    post = Post.objects.filter(pk=post_id)
    context = {'post':post}
    return render(request,'blog/single_post.html',context=context)
@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('posts'))
    else:
        form = PostForm()
    context = {'form':form}
    return render(request,'blog/add_post.html',context=context)
@login_required
def profile(request):
    user = Users.objects.all()
    context = {'user':user}
    return render(request,'blog/profile.html')