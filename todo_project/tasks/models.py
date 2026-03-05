from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, blank=False)
    description =  models.TextField( blank=False)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now) # по москве
    
    def __str__(self):
        return self.title