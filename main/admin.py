from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    
    # Для не-суперпользователей
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['name', 'email', 'message', 'created_at']
        return []
