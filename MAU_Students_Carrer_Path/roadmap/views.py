# views.py
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Roadmap, Course
from django.contrib import messages# views.py
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def homepage(request):
    return render(request, 'pages/index.html')

def index(request):
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    context = {
        'greeting': greeting,
        'user_name': request.user.username, 
        'university_message': "Thank you for choosing Modibbo Adama University, Yola! Feel free to browse the page and explore the resources available."
    }
    
    return render(request, 'pages/homepage.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return HttpResponseRedirect(request.path)
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return HttpResponseRedirect(request.path)
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('login')
    
    return render(request, 'pages/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid credentials")
            return render(request, 'pages/login.html') 
    else:
        return render(request, 'pages/login.html') 
    
@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        roadmaps = Roadmap.objects.filter(career_path__icontains=query)
    else:
        roadmaps = Roadmap.objects.all()  # List all roadmaps if no query

    return render(request, 'pages/search.html', {'roadmaps': roadmaps})

@login_required
def roadmap_detail(request, roadmap_id):
    roadmap = Roadmap.objects.get(id=roadmap_id)
    courses = roadmap.courses.all()
    return render(request, 'pages/roadmap_details.html', {'roadmap': roadmap, 'courses': courses})

def custom_permission_denied(request, *args, **kwargs):
    return render(request, 'pages/403.html', status=403)


def restricted(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'pages/restricted.html')

def logout_view(request):
    logout(request)
    return redirect('login')

