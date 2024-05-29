from django.contrib import admin
from .models import ArchivoCsv

# Register your models here.

class ArchivoCsvAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(ArchivoCsv, ArchivoCsvAdmin)