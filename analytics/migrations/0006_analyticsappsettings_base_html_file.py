# Generated by Django 2.2.5 on 2024-03-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0005_analyticsappsettings"),
    ]

    operations = [
        migrations.AddField(
            model_name="analyticsappsettings",
            name="base_html_file",
            field=models.URLField(help_text="htmlファイルのベースとなるファイル名を入力してください。プロジェクト直下の場合は「base.html」。アプリ直下の場合は「app/base.html」。", max_length=100, null=True, verbose_name="ベースファイル"),
        ),
    ]
