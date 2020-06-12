from django.db import models

# Create your models here.
class Thing(models.Model):
    title=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    text=models.TextField()
    th_time=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)