from django.contrib import admin
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone', ]


@admin.register(UserProfile)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'age', 'phone_number']
