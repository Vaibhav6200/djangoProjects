from django.urls import path
from AppTwo import views

app_name = "AppTwo"

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
    path("adduser/", views.addUser, name="add_new_user"),
    path("signup/", views.signup, name="signup"),
]