from django.contrib import admin
from hotels.models import Hotel
# Register your models here.

@admin.register(Hotel)
class ProfileAdmin(admin.ModelAdmin):
   """Profile admin."""
   list_display = ('city')
   list_display_links = ('pk', 'hotel',)
   list_editable = ('city')
   search_fields = (
       'city'
   )
   list_filter = (
       'city',
   )
