from django.db import models

# Create your models here.
class UserData(models.Model):
    phone = models.CharField(max_length=32, unique=True)
    last_balance = models.IntegerField(default=0)
    telegram_id = models.CharField(max_length=32, null=True)
    
