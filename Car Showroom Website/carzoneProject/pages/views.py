from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'pages/index.html')

def about(request):
     return render(request, 'pages/about.html')

def car(request):
     return render(request, 'pages/car.html')

def services(request):
     return render(request, 'pages/services.html')

def contact(request):
     return render(request, 'pages/contact.html')

def login(request):
     return render(request, 'pages/login.html')

def signup(request):
     return render(request, 'pages/signup.html')