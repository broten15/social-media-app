from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """Picutre with description which is shown on the feed"""
    description = models.CharField(max_length=400)
    pic = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        """String for representing the Model object."""
        return "post"