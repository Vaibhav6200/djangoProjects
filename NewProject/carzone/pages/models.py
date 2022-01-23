from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img')
    instagram_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)

    def __str__(self):
        return self.first_name