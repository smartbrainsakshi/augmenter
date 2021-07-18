from django.contrib import admin

# Register your models here.

from .models import Parent, Negative, Positive

admin.site.register([Parent, Negative, Positive])
