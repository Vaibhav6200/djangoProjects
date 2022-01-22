from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm,UserForm

# importing some modules for user login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

# since we want to show this option only when a user is logged in so we will use decorators
@login_required
def user_logout(request):
    # we will pass our request to built in logout function which will automatically logout our user
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    profile_form = UserProfileInfoForm()
    user_form = UserForm()
    registered = False

    if request.method == "POST":
        # if request method is post then we are grabbing all information from the forms in variables, user_form and profile_form
        profile_form = UserProfileInfoForm(request.POST)
        user_form = UserForm(request.POST)

        # Now checking if both forms are valid or not
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)     # if commit=False then information will not be committed to the database
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    return render(request, 'basic_app/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Now we will use django authentication function, so it will authenticate our user
        user = authenticate(username=username, password=password)

        # Now if we have a user (i.e. if it has been authenticated)
        if user:
            if user.is_active:  # now checking if users account is active
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Invalid Login Details Supplied!")
    else:
        return render(request, 'basic_app/login.html')