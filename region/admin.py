from django.contrib import admin
from .models import *


class RegionInline(admin.TabularInline):
    model = ClassifiedRegion


class RegionAdmin(admin.ModelAdmin):
    model = Region
    inlines = [RegionInline]


admin.site.register(Region, RegionAdmin)
admin.site.register(ClassifiedRegion)
