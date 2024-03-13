# Generated by Django 2.2.5 on 2024-03-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0004_auto_20240304_1746"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnalyticsAppSettings",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nav_title", models.CharField(help_text="ナビゲーションバーの左上に表記される文字", max_length=50, verbose_name="ナビゲーションのタイトル")),
                ("heading_ja", models.CharField(help_text="画面中央頭に表記される見出し。日本語で記入してください。", max_length=100, verbose_name="日本語の見出し")),
                ("heading_us", models.CharField(help_text="画面中央頭に表記される見出し。英語で記入してください。", max_length=100, verbose_name="英語の見出し")),
            ],
        ),
    ]
