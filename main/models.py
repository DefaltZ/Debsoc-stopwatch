from django.db import models

class SiteConfiguration(models.Model):
    college_name = models.CharField(max_length=200)
    motto = models.CharField(max_length=200, blank=True)
    additional_text = models.TextField(blank=True)
    logo = models.ImageField(upload_to='logos/')
    background = models.ImageField(upload_to='backgrounds/')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return f"Site Configuration - {self.updated_at}"