from django.contrib import admin
from contact.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'client_email', 'car_title', 'created_date']
    list_display_links = ['id', 'firstname', 'lastname']
    search_fields = ['id', 'car_title', 'client_email', 'firstname', 'lastname']
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)