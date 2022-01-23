from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model  = User
        # fields = '__all__'
        fields = ('username', 'first_name' , 'last_name', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        # fields = '__all__'
        fields = ('portfolio_site', 'profile_pic')