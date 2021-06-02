from django.contrib import admin

from pathology.models import Plant
from django.contrib.auth.admin import UserAdmin

admin.site.register(Plant)
