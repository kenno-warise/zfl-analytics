from django.test import TestCase  # type: ignore
from django.utils import timezone  # type: ignore

from analytics.models import AnalyticsAppSettings, DimensionDate


class AnalyticsAppSettingsTests(TestCase):
    """AnalyticsAppSettingsモデル"""

    def test_base_index_html_save(self):
        """base_index_htmlフィールドの値が変更され保存された際のテスト"""

        import os
        import re

        from django.conf import settings  # type: ignore

        basehtml_file = "analytics/templates/analytics/base_index.html"
        file_dir = os.path.join(settings.BASE_DIR, basehtml_file)
        with open(file_dir) as f:
            html_text = f.read()
        base_html_file = "analytics/base.html"
        existing_name = re.search("^" + base_html_file, html_text)
        if not existing_name:
            AnalyticsAppSettings.objects.create(base_html_file=base_html_file)
        # アサートに使用する値
        aas = AnalyticsAppSettings.objects.all().first()
        with open(file_dir) as f:
            html_text = f.read()
        comp = re.compile(r"extends '\w+.html|extends '\w+/\w+.html")
        re_obj = comp.search(html_text)
        if re_obj:
            html_text = re_obj.group().replace("extends '", "")
        # Assert
        self.assertEqual(aas.base_html_file, html_text)
        # extends 'analytics/base.html'になってしまったのを戻す
        aas.base_html_file = "base.html"
        aas.save()


class DimensionDateTests(TestCase):
    """DimensionDateモデル"""

    def test_str_method_returns_dates(self):
        """
        strメソッドではdatesの値が返される。
        """

        date = timezone.now().date()
        dimensiondate = DimensionDate(
            dates=date,
            users=1,
            new_users=1,
            page_views=1,
            sessions=1,
            ad_revenue=1,
            ad_impressions=1,
        )
        self.assertEqual(dimensiondate.__str__(), str(date))
