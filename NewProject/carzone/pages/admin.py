from django.contrib import admin
from pages.models import Team

# we want to display icon(image of user) near id so we imported this module
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius : 50%;" />'.format(object.photo.url))

    thumbnail.short_description = 'Photo'   # so our photos will be displayed under Photo section (we have renamed this section from "thumbnail" -> "Photo")

    # these fields will be displayed in our admin pannel
    list_display = ('id','thumbnail', 'first_name', 'last_name', 'designation')

    # we want to make our first_name clickable so we added this code
    list_display_links = ('first_name', 'id', 'thumbnail')

    # This will add a search bar in our admin pannel based on first name and last name
    search_fields = ('first_name', 'last_name')

    # This will add a filter section on our admin pannel based on designation
    list_filter = ('designation',)     # we added comma because it accepts a tuple

admin.site.register(Team, TeamAdmin)
