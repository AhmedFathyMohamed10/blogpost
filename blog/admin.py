from django.contrib import admin
from .models import *
# Register your model
# s here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)