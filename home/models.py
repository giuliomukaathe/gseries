from django.db import models

# Create your models here.

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    role = models.CharField(max_length=100)
    twitterlink = models.URLField(blank=True)
    facebooklink = models.URLField(blank=True)
    tiktoklink = models.URLField(blank=True)
    instagramlink = models.URLField(blank=True)

    def __str__(self):
        return self.name

