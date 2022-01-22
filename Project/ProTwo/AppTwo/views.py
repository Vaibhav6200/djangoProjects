from django.forms import forms
from django.shortcuts import render
from AppTwo.models import User
from AppTwo.forms import FormName, NewUser


# Create your views here.
def index(request):
    my_dict = {'text': "Hello World, I am Vaibhav Paliwal", 'number': 308}
    return render(request, 'appTwo/index.html', my_dict)


def users(request):
    user_list = User.objects.order_by("first_name")
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', user_dict)


def formpage(request):
    form = FormName()   # creating a form using forms.py file and sending that form to our html page where we will use template tags to display it on screen
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            # Do some code
            print("Validation Success, its a POST request")
            print("Name : " + form.cleaned_data['name'])
            print("Email : " + form.cleaned_data['email'])
            print("Text : " + form.cleaned_data['text'])
    return render(request, "appTwo/form_page.html", {'form': form})


def addUser(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)      # use commit to commit it to database
            return index(request)
        else:
            print("Error! Form Invalid")
    return render(request, "appTwo/form_page.html", {'form': form})



def signup(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignnupForm()
        fname = form.cleaned_data['first_name']
        lname = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
    return render(request, 'appTwo/signup.html',  {'form': form})

