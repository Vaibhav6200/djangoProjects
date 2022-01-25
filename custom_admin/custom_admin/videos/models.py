from django.db import models

# Create your models here.
class customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class movie(models.Model):
    title = models.CharField(max_length=128)
    length = models.PositiveIntegerField()
    released_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title