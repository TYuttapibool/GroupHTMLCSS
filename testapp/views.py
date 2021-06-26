from django.shortcuts import render, redirect

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def other(request):
    return render(request, 'otherprofile.html')

def summary(request):
    return render(request, 'summary.html')

def history(request):
    return render(request, 'history.html')

def pool(request):
    return render(request, 'pool.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')