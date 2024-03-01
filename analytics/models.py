from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models


class GoogleAnalytics4Config(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    property_id = models.PositiveIntegerField()
    days_ago = models.PositiveIntegerField(default=7, validators=[MaxValueValidator(30)])

    def __str__(self):
        author = str(self.author)
        return author


class DimensionDate(models.Model):
    dates = models.DateField()  # 西暦と月日を保存
    users = models.PositiveIntegerField()  # 0と正の整数を保存
    new_users = models.PositiveIntegerField()
    page_views = models.PositiveIntegerField()
    sessions = models.PositiveIntegerField()
    ad_revenue = models.PositiveIntegerField()
    ad_impressions = models.PositiveIntegerField()

    def __str__(self):
        dates = str(self.dates)
        return dates

# Create your models here.
