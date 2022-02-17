import datetime

from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    client_needs = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=128)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(default=datetime.datetime.now())

    # Fields which will help us connecting with database
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=128)
    user_id = models.IntegerField()

    def __str__(self):
        return self.client_email

