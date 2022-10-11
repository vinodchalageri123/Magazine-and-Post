from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)
    ordering = ['author']
    search_fields = ('title', 'author',)


admin.site.register(Category)
admin.site.register(Comment)
