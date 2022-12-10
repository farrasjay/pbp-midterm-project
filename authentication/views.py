from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('authentication:index')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def login_flutter(request):
    # print("MASUK DISINI")
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    if request.method == 'POST':
        user = authenticate(username=username, password=password)
        # print("AUTENTHICATE")
        # print(username)
        # print(password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": True,
                "username": request.user.username,
                "message": "Successfully Logged In!"
            }, status=200)

        else:
             return JsonResponse({
                "status": False,
                "message": "Failed to Login!"
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, your username/password may be wrong."
        }, status=401)

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

@csrf_exempt
def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)