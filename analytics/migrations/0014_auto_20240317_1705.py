# Generated by Django 2.2.5 on 2024-03-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0013_auto_20240316_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleanalytics4config',
            name='property_id',
            field=models.CharField(max_length=150, verbose_name='プロパティID'),
        ),
    ]
