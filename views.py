from django.shortcuts import render, redirect


def index(request):
    if request.method=='POST':
        username=request.POST('username')
        password=request.POST('password')
        from django.contrib import auth
        x=auth.authenticate(username=username,password=password)
        if x is None:
            return redirect("login")
        else:
            return redirect('page1')
    else:

      return render(request,'index.html')
def login(request):
    return render(request,'page1.html')
