from django.shortcuts import render, redirect
from pages.models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True)
    all_cars = Car.objects.all()
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    models_search = Car.objects.values_list("model", flat=True).distinct()
    city_search = Car.objects.values_list("city", flat=True).distinct()
    year_search = Car.objects.values_list("year", flat=True).distinct()
    body_style_search = Car.objects.values_list("body_style", flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'models_search': models_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        # 'search_fields': search_fields,
    }
    return render(request, 'pages/index.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        email_subject = "You have a new message from carzone website regarding: " + subject
        email_message_body = "Name: " + name + " \nEmail: " + email + " \nPhone: " + phone + " \nMessage: " + message
        # SENDING MAIL TO ADMIN
        send_mail(
            email_subject,  # subject of email
            email_message_body,     # message body of email
            'vaibhavpaliwal620@gmail.com',      # from which email id email will be sent
            [admin_email],      # TO : which email will be sent
            fail_silently=False
        )
        messages.success(request, "Thank You for contacting us. We will get back to you shortly")
        return redirect('pages:contact')

    return render(request, 'pages/contact.html')