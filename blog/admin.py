from django.contrib import admin
from .models import Post

# Register your models - this will make them visible on admin pg
admin.site.register(Post)