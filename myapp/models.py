from django.db import models
from django.forms import DateField

# Create your models here.


class ToDo(models.Model):
    Title = models.CharField(max_length=50, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Title
