
import datetime, json
from distutils.command.clean import clean
import imp
import datetime, json, logging
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserHealthStatus
from .forms import HealthStatsForm
from django.views.decorators.csrf import csrf_exempt

def landingpage(request):
    return render(request, 'home.html')

def register(request):
    # logger = logging.getLogger(__name__)
    # logger.debug("MASUK REGISTER")
    # print("MASUK REGISTER")
    form = UserCreationForm()

def register(request):
    form  = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('uhealths:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("uhealths:menu"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('uhealths:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/uhealths/login/')
def main_menu(request):
    return render(request, "menu.html")

@login_required(login_url='/uhealths/login/')
def show_healthstats(request):
    return render(request, "show_healthstats.html")

def insert_healthstats(request):
    form = HealthStatsForm()
    context = {'form':form}
    return render(request, 'insert_healthstats.html', context)

def calculate_bmi(height, weight):
    bmi = weight/(height/100)**2
    return bmi

def calculate_bmr(gender, age, height, weight):
    bmr = 0.0
    if gender.upper() == 'MALE':
        bmr = 66.5  + (13.7 * weight) + (5 * height) - (6.7 * age)
    elif gender.upper() == 'FEMALE':
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    return bmr

def show_json(request):
    data = serializers.serialize("json", UserHealthStatus.objects.all())
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='/uhealths/login/')
def show_healthstats_ajax(request):
    # print(request.user)
    healthstats_data = UserHealthStatus.objects.filter(user = request.user).order_by('-last_update')[:10]
    response = serializers.serialize("json", healthstats_data)
    return HttpResponse(response, content_type="application/json")

@csrf_exempt
def show_healthstats_json(request):
    # print(request)
    healthstats_data = UserHealthStatus.objects.filter(user_id = request.POST['user_id']).order_by('-last_update')[:10]
    response = serializers.serialize("json", healthstats_data)
    return JsonResponse({"data" : response})

@login_required(login_url='/uhealths/login/')
def post_healthstats_ajax(request):
    if request.method == 'POST':
        last_update = datetime.datetime.now()
        height = float(request.POST['height'])
        weight = float(request.POST["weight"])
        age = float(request.POST["age"])
        gender = request.POST["gender"]
        calories_intake = request.POST["calories_intake"]
        
        # print("USER : " + request.user.id)
        instance = UserHealthStatus(user = request.user, gender = gender, age = age, height = height, weight = weight, calories_intake = calories_intake, bmr = calculate_bmr(gender, age, height, weight), bmi = calculate_bmi(height, weight), last_update = last_update)
        instance.save()
        
        data = {
            "message": 'Healthstat submitted successfully!'
        }
        json_object = json.dumps(data, indent = 4) 

        return JsonResponse(json.loads(json_object))
    return redirect("uhealths:insert_healthstats")

@csrf_exempt
def insert_healthstats_flutter(request):
    data = json.loads(request.body)
    
    last_update = datetime.datetime.now()
    height = float(request.POST['height'])
    weight = float(request.POST["weight"])
    age = float(request.POST["age"])
    gender = request.POST["gender"]
    calories_intake = request.POST["calories_intake"]

    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        instance = UserHealthStatus(user = user, gender = gender, age = age, height = height, weight = weight, calories_intake = calories_intake, bmr = calculate_bmr(gender, age, height, weight), bmi = calculate_bmi(height, weight), last_update = last_update)
        instance.save()
        return JsonResponse({
                "status": True,
                "message": "Successfull!"
            }, status=200)
    return JsonResponse({
            "status": False,
            "message": "Failed!"
    }, status=502)