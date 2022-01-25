from django.contrib import admin
from videos import models

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields = ['released_year', 'title', 'length']
    search_fields = ['title', 'length']
    list_filter = ['released_year', 'length']
    list_display = ['id', 'title', 'length', 'released_year']
    list_editable = ['length', 'released_year']

admin.site.register(models.customer)
admin.site.register(models.movie, MovieAdmin)
