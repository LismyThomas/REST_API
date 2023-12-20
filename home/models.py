from django.db import models


# Create your models here.
class Person(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
def __str__(self):
        return f"{self.title}"