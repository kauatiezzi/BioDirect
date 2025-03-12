from django.contrib import admin
from .models import Item
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Item)
