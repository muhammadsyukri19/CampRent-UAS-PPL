from django.contrib import admin
from .models import Equipment, Booking


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_per_day', 'stock', 'created_at']
    list_filter = ['category']
    search_fields = ['name', 'description']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'equipment', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['customer_name', 'phone']
