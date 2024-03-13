# Generated by Django 2.2.5 on 2024-03-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0007_auto_20240309_1826"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analyticsappsettings",
            name="base_html_file",
            field=models.CharField(blank=True, help_text="htmlファイルのベースとなるファイル名を入力してください。プロジェクト直下の場合は「base.html」。アプリ直下の場合は「app/base.html」。", max_length=100, null=True, verbose_name="ベースファイル"),
        ),
    ]
