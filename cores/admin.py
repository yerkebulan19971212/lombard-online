# django imports
from django.contrib import admin

# local import
from .models import Category


admin.site.register((Category, ))
