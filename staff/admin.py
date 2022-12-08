from django.contrib import admin
from .models import AboutStaff, Contacts

admin.site.register(AboutStaff)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['text', 'email', 'phone_number']



