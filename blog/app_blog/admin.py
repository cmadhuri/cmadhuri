from django.contrib import admin

from app_blog.models import blogpage,login

# Register your models here.
admin.site.register(login)
admin.site.register(blogpage)

