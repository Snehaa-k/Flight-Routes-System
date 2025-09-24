from django.contrib import admin
from django.contrib import admin
from .models import Airport,Route
# Register your models here.



@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ("code",)
    search_fields = ("code",)

@admin.register(Route)
class AirportRouteAdmin(admin.ModelAdmin):
    list_display = ("source", "destination", "position", "duration")
    list_filter = ("position",)
    search_fields = ("source__code", "destination__code")
