from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
# Create your models here.

class UserModels(AbstractUser):
    account  = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

@admin.register(UserModels)
class UserAdminModel(admin.ModelAdmin):
    list_display = ("account","role")