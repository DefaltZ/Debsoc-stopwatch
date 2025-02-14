from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import SiteConfiguration

# Customize admin header and title
admin.site.site_header = 'Debsoc Stopwatch Admin'
admin.site.site_title = 'Debsoc Admin Portal'
admin.site.index_title = 'Welcome to Debsoc Stopwatch Administration'

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'updated_at')
    
    def has_add_permission(self, request):
        # Only allow one configuration
        if self.model.objects.exists():
            return False
        return True