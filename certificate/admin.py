from django.contrib import admin
from .models import OrderCertificate


@admin.register(OrderCertificate)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'tours', 'info', 'count_people', 'email', 'phone', 'sender', 'addressee', 'paid']


