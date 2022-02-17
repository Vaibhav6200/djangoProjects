from django.shortcuts import render, redirect
from contact.models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        client_needs = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        client_email = request.POST['customer_email']
        client_phone = request.POST['customer_phone']
        message = request.POST['message']
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']

        # CHECKING FOR EXISTING ENQUIRY
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already inquired about the car")
                return redirect('/cars/' + car_id)


        # SAVING INQUIRY IN DATABASE
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, firstname=firstname, lastname=lastname, client_needs=client_needs, client_phone=client_phone, client_email=client_email, city=city, state=state, message=message)

        # ALERT ADMIN FOR INQUIRY via MAIL Before saving Inquiry in database
        admin_info = User.objects.get(is_superuser=True)
        admin_email=admin_info.email

        send_mail(
            'New Car Inquiry',      # subject of email
            'You have a new inquiry for the car ' + car_title + " please Login to you admin pannel for more info",      # email body
            'vaibhavpaliwal620@gmail.com',      # FROM : which email id we want to send this message
            [admin_email],  # TO : which email id this mail will be sent
            fail_silently=False
        )

        contact.save()
        messages.success(request, "Your request has been Submitted, we will contact you soon")
        return redirect('/cars/' + car_id)


