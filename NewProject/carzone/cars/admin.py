from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html

class carAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50px" style="border-radius: 50%; " />'.format(object.car_photo.url))

    thumbnail.short_description = "car photo"
    list_display = ['id', 'thumbnail', 'car_title', 'model', 'color', 'price', 'body_style', 'fuel_type', 'is_featured']
    list_display_links = ['id', 'thumbnail', 'car_title']
    search_fields = ['car_title', 'color', 'fuel_type', 'model']
    list_filter = ['color', 'fuel_type', 'body_style']
    list_editable = ['is_featured']

# Register your models here.
admin.site.register(Car, carAdmin)
