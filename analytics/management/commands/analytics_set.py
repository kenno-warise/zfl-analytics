from django.core.management.base import BaseCommand

from analytics.models import AnalyticsAppSettings


class Command(BaseCommand):
    # 本日から数日前までのデータを保存する

    def handle(self, *args, **options):
        try:
            AnalyticsAppSettings.objects.create(
                    nav_title="アナリティクス",
                    heading_ja="ようこそアナリティクスページへ",
                    heading_us="Welcome to analytics page",
            )
            self.stdout.write(self.style.SUCCESS("アナリティクスアプリの初期設定完了"))
        except:
            self.stdout.write(self.style.ERROR("先に「python3 manage.py migrate」を実行してください"))

