from django.contrib import admin
from .models import UserDetails,Gender

# Register your models here.

admin.site.register(UserDetails)
admin.site.register(Gender)