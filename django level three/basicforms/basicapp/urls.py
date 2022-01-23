from basicapp import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path("formpage/", views.form_name_view, name='form_name'),
]
