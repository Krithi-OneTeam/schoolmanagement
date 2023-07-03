from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your views here.

def log_vw(request):
    return render(request,'authentication/login_success.html')


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/member/lg_su/')
    return render(request,'authentication/login.html')



def home(request):
    return render(request,'home.html')
            