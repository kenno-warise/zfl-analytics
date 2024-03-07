from django.contrib import admin

from .models import AnalyticsAppSettings, GoogleAnalytics4Config, DimensionDate


admin.site.register(AnalyticsAppSettings)
admin.site.register(GoogleAnalytics4Config)
admin.site.register(DimensionDate)

# Register your models here.
