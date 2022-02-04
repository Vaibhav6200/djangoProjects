from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=50)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
