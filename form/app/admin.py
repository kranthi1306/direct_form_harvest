from django.contrib import admin
from .models import User, Crop, Request

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'role', 'is_verified')
    search_fields = ('phone', 'name')
    list_filter = ('role', 'is_verified')

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity', 'farmer')
    search_fields = ('name',)
    list_filter = ('farmer',)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'crop', 'message')
    search_fields = ('buyer__name', 'crop__name')
    list_filter = ('crop__name',)
