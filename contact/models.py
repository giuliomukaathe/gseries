from django.db import models
from django.utils import timezone
# Create your models here.

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    message_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
