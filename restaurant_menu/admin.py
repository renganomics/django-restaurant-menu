from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("meal", "status", "meal_type")
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)