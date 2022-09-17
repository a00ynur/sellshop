from django.contrib import admin
from core.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_filter = ['name', 'email']
    list_display = ['name', 'email', 'created_at']