from django.contrib import admin
from .models import Tour, Types, Entry, Comment, Category, Like


admin.site.register(Types)
admin.site.register(Category)
admin.site.register(Like)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


class EntryInline(admin.StackedInline):
    model = Entry
    fields = ['user', 'date_buy', 'get_user_phone']
    readonly_fields = ['date_buy', 'get_user_phone']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [EntryInline]
    # pass
