from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # create relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # add any additional attributes
    portfolio_site = models.URLField(blank=True)   # if blank=True: means we are saying django that if user did not specify this field then its OK, no need to force him
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
