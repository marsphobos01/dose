from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def default_time_taken():
    return timezone.make_aware(datetime(2000, 1, 1))


class Med(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.IntegerField()
    unit = models.CharField(max_length=20,default="mg")
    daily_amount = models.IntegerField()
    total_amount = models.IntegerField()
    start_date = models.DateField(null=True,blank=True)
    expiration_date = models.DateField(null=True,blank=True)
    notes = models.TextField(null=True,blank=True)
    time_taken = models.DateTimeField(default=default_time_taken)

    def __str__(self):
        return f"{self.id} - {self.name}, {self.dosage}{self.unit}"


    @property
    def can_take(self):
        if self.time_taken is None:
            return True
        return self.time_taken.date() < timezone.localdate()

    @property
    def is_expiring_soon(self):
        return self.expiration_date <= timezone.now().date() + timedelta(days=7)

    @property
    def has_taken_today(self):
        if not self.time_taken:
            return False
        return self.time_taken.date() == timezone.now().date()

    @property
    def can_mark_taken(self):
        return not self.has_taken_today

    def mark_taken(self):
        if self.can_take:
            self.time_taken = timezone.now()
            self.total_amount = max(self.total_amount - self.daily_amount, 0)
            self.save(update_fields=["time_taken", "total_amount"])
