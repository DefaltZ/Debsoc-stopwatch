from django.contrib import admin
from .models import SiteConfiguration

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'updated_at')
    
    def has_add_permission(self, request):
        # Only allow one configuration
        if self.model.objects.exists():
            return False
        return True