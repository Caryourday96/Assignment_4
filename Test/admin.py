from django.contrib import admin
#Last Modified 23rd March
#ADETUNJI KAYODE
#Models are registered and referenced here
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Industry

@admin.register(Industry)
class IndustryAdmin(ImportExportModelAdmin):
    pass
