from django.core.management.base import BaseCommand

from analytics.update_api import update_data


class Command(BaseCommand):
    # 本日から数日前までのデータを保存する

    def handle(self, *args, **options):
        try:
            update_data.update_analyticsdata()
            self.stdout.write(self.style.SUCCESS('アナリティクスアプリのデータベース更新完了'))
        except:
            self.stdout.write(self.style.ERROR('GoogleAnalytics4の設定が完了しておりません'))

