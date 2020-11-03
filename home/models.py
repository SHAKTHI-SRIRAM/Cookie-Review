from django.db import models
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

