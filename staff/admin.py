from django.contrib import admin
from .models import AboutStaff, Contacts

admin.site.register(AboutStaff)
admin.site.register(Contacts)

@admin.site.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_diplay = ['text', 'email', 'phone_number']
