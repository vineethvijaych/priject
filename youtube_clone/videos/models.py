from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    views = models.PositiveIntegerField()
    upload_date = models.DateField()
    thumbnail = models.ImageField(upload_to='thumbnails/')  
    author_image = models.ImageField(upload_to='thumbnails/',null=True) 
    link = models.CharField(max_length=255,null=True)

    




