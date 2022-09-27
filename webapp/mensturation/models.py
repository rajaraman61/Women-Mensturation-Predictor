from tkinter import CASCADE
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_project import settings


class Period(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    age = models.IntegerField(default=0)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    duration = models.FloatField(default=0)
    heart_rate = models.FloatField(default=0)
    average_heart_rate_per_day = models.FloatField(default=0)
    average_body_temp_per_day = models.FloatField(default=0)
    average_calories_burnt_per_day = models.FloatField(default=0)
    

@receiver(post_save, sender=User)
def create_user_period(sender, instance, created, **kwargs):
    if created:
        Period.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_period(sender, instance, **kwargs):
    instance.period.save()