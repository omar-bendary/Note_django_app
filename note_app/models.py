from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.title
