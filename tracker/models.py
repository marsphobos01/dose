from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.

class Med(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.IntegerField()
    unit = models.CharField(max_length=20,default="mg")
    daily_amount = models.IntegerField()
    total_amount = models.IntegerField()
    start_date = models.DateField(null=True,blank=True)
    expiration_date = models.DateField(null=True,blank=True)
    notes = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}, {self.dosage}{self.unit}"

    @property
    def is_expiring_soon(self):
        return self.expiration_date <= timezone.now().date() + timedelta(days=7)
