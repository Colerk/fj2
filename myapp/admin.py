from django.contrib import admin
from .models import JournalRecord, Profile
# Register your models here.

admin.site.register(JournalRecord)
admin.site.register(Profile)