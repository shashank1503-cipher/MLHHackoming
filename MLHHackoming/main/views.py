from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db.models import Q
from .forms import PostForm
# Create your views here.
from .models import Post
def home(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'main.html',{'posts' : posts})
"""def like(request,id):
    if request.method == 'POST':
        obj = Likes.objects.filter(post_id=id)
        user = getattr(obj,'user')
        if user != request.user.username:
            like = Likes(post_id=id,user=user)
"""

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_title = form.cleaned_data['postTitle']
            post_desc = form.cleaned_data['postDesc']
            post_content = form.cleaned_data['postContent']
          
            p = Post(postContent= post_content,postTitle = post_title,postDesc = post_desc,user=request.user.username,userName=request.user.get_short_name())
            p.save()
            return redirect('/main')
    else:
        form = PostForm()
    return render(request,'write.html',{'form': form})

def detail(request,id):
    posts = Post.objects.filter(id = id)
    return render(request,'detail.html',{'posts' : posts})   
def search(request):        
    if request.method == 'GET':      
        query =  request.GET.get('searchId') 
        print(query)               
        posts = Post.objects.filter(Q(postTitle__icontains = query) | Q(postContent__icontains = query))
        return render(request,'search.html',{'posts':posts})
    else:
        return render(request,"search.html",{})
def userRecipe(request):
    posts = Post.objects.filter(user = request.user.username)
    return render(request,'userrecipe.html',{'posts':posts})
