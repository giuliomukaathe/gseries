from django.db import models
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    package = models.CharField(max_length=20, choices=[('bronze', 'Bronze Package'), ('platinum', 'Platinum Package'), ('royal', 'Royal Package')])
    additional_comments = models.TextField(blank=True)
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
