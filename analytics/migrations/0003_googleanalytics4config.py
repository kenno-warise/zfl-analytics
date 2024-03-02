# Generated by Django 3.2.24 on 2024-03-01 07:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0002_auto_20240229_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalytics4Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.PositiveIntegerField()),
                ('days_ago', models.PositiveIntegerField(default=7, validators=[django.core.validators.MaxValueValidator(30)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]