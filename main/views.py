from django.shortcuts import render
from .models import SiteConfiguration

def index(request):
    config = SiteConfiguration.objects.first()
    return render(request, 'main/index.html', {'config': config})