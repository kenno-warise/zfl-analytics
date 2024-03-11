from django.contrib import admin
from django.shortcuts import redirect

from .models import AnalyticsAppSettings, GoogleAnalytics4Config, DimensionDate


class AnalyticsAppSettingsAdmin(admin.ModelAdmin):
    save_on_top = True
    fieldsets = (
            ("ベースHTMLファイル設定", {
                "fields": ("base_html_file",)
            }),
            ("ページの編集", {
                "fields": ("nav_title", "heading_ja", "heading_us")
            }),
            ("レイアウトの調整", {
                "fields": ("container", ("col_left", "col_center", "col_right"),)
            }),
    )


admin.site.register(AnalyticsAppSettings, AnalyticsAppSettingsAdmin)
admin.site.register(GoogleAnalytics4Config)
admin.site.register(DimensionDate)

# Register your models here.
