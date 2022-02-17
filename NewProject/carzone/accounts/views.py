from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        login_password = request.POST['password']
        user = auth.authenticate(username=username, email=email, password=login_password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("accounts:dashboard")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("accounts:login")

    return render(request, 'accounts/login.html')

def register(request):
    # we have to check for 3 validations
    # (i) Password and confirmPassword should match
    # (ii) username id should be unique
    # (iii) email id should be unique
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                auth.login(request, user)
                user.save()
                messages.success(request, "You are Successfully Registered!")
                return redirect("accounts:dashboard")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'accounts/register.html')

@login_required(login_url = 'accounts:login')
def dashboard(request):
    filtering_user_inquiries = Contact.objects.filter(user_id = request.user.id)
    inquiry_info = {
        'inquiry_info': filtering_user_inquiries,
    }

    return render(request, 'accounts/dashboard.html', inquiry_info)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("pages:index")
