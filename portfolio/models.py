from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
    
class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=100, default='type...')
    video_link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
