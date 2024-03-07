from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models


class AnalyticsAppSettings(models.Model):
    nav_title = models.CharField(
            verbose_name="ナビゲーションのタイトル",
            max_length=50,
            help_text="ナビゲーションバーの左上に表記される文字"
    )
    heading_ja = models.CharField(
            verbose_name="日本語の見出し",
            max_length=100,
            help_text="画面中央頭に表記される見出し。日本語で記入してください。"
    )
    heading_us = models.CharField(
            verbose_name="英語の見出し",
            max_length=100,
            help_text="画面中央頭に表記される見出し。英語で記入してください。"
    )

    def __str__(self):
        return self.nav_title


class GoogleAnalytics4Config(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    property_id = models.PositiveIntegerField()
    days_ago = models.PositiveIntegerField(default=7, validators=[MaxValueValidator(30)])

    def __str__(self):
        author = str(self.author)
        return author


class DimensionDate(models.Model):
    dates = models.DateField(verbose_name="日付")  # 西暦と月日を保存
    users = models.PositiveIntegerField(verbose_name="アクセス数")  # 0と正の整数を保存
    new_users = models.PositiveIntegerField(verbose_name="新規ユーザー数")
    page_views = models.PositiveIntegerField(verbose_name="ページビュー数")
    sessions = models.PositiveIntegerField(verbose_name="セッション数")
    ad_revenue = models.PositiveIntegerField(verbose_name="広告収益")
    ad_impressions = models.PositiveIntegerField(verbose_name="インプレッション数")

    def __str__(self):
        dates = str(self.dates)
        return dates

# Create your models here.
