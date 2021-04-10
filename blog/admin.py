from django.contrib import admin
from .models import post

# Register your models here.
# admin.site.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'date_posted')

admin.site.register(post, PostAdmin)