from django.utils import timezone
from django.db import models

# Create your models here.

CHARS_MAX_LENGTH: int = 150

class Tag(models.Model):
    """Tag model class."""
    def __str__(self):
        return self.name

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)


#Category Table
class Category(models.Model):
    """Category model class."""
    def __str__(self):
        return self.name

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)


#Movies  Table    
class Movie(models.Model):
    """Movie model class."""
    def __str__(self):
        return self.name

    name = models.CharField(max_length=CHARS_MAX_LENGTH, blank=True)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    #We'll suppose that a movie just belong to one category (a OneToMany relationship)
    category = models.ForeignKey( Category, models.CASCADE )
    #now in this case, a movie could have many tags, so that mens a ManyToMany relationship
    tags = models.ManyToManyField(Tag)
    #Count to kwon how many peapople watch a movie
    watch_count = models.IntegerField(default=0)
    file = models.FileField(upload_to='movies/')
    preview_image = models.ImageField(upload_to='preview_images/')
