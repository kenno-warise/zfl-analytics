# Generated by Django 2.2.5 on 2024-03-10 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0009_auto_20240309_2305"),
    ]

    operations = [
        migrations.AddField(
            model_name="analyticsappsettings",
            name="col_center",
            field=models.PositiveIntegerField(default=12),
        ),
        migrations.AddField(
            model_name="analyticsappsettings",
            name="col_left",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="analyticsappsettings",
            name="col_right",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="analyticsappsettings",
            name="container",
            field=models.CharField(default="container", max_length=15),
        ),
    ]
