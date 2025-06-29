from django.contrib import admin
from .models import Contact

# Register your models here.

admin.site.site_header = "Contact Management Admin"
admin.site.site_title = "Contact Management Admin Portal"
admin.site.index_title = "Welcome to the Contact Management System Admin Portal"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Contact, ContactAdmin)
