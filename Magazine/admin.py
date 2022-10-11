from django.contrib import admin
from .models import Magazines, MyClubUser


# Register your models here.
admin.site.register(MyClubUser)


class MagazinesAdmin(admin.ModelAdmin):
    list_display = ('magazine_name', 'published_at', 'magazine_copy')
    ordering = ['published_at']
    search_fields = ('magazine_name', 'published_at')


admin.site.register(Magazines, MagazinesAdmin)


# @admin.register(Magazines)
# class MagazinesAdmin(admin.ModelAdmin):
#     list_display = ('magazine_name', 'published_at', 'magazine_copy')
#     ordering = 'published_at'
#     search_fields = ('magazine_name', 'published_at')
