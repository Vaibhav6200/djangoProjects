from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.index, name='home'),
]