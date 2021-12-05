from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    else:
        return render(request,'index.html')
def login(request):
        if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['pwd']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('main:home')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else:
            return redirect('index')
       
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        cpwd = request.POST['Cpwd']
        email = request.POST['email']
        username = email
        if pwd == cpwd:
            if(User.objects.filter(username= username).exists()):
                messages.info(request,'Email already there')    
                return redirect('signup')
            else:        
                user = User.objects.create_user(username = username, password = pwd,first_name = name,email= email)
                user.save()
                return redirect('main:home')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
def about(request):
    return render(request,'aboutus.html')
def concept(request):
    return render(request,'concept1.html')
def contact(request):
    return render(request,'contactUs.html')