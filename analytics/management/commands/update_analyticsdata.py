from django.core.management.base import BaseCommand  # type: ignore

from analytics.update_api import update_data


class Command(BaseCommand):
    # 本日から数日前までのデータを保存する

    def handle(self, **options):  # noqa: ARG002
        try:
            update_data.update_analyticsdata()
            success_text = "アナリティクスアプリのデータベース更新完了"
            self.stdout.write(self.style.SUCCESS(success_text))
        except Exception as inst:
            Exception(inst)
            error_text = "GoogleAnalytics4の設定が完了しておりません"
            self.stdout.write(self.style.ERROR(error_text))
