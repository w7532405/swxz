from django.db import models

# Create your models here.
class DayShare(models.Model):
    share_time=models.DateTimeField(auto_now=True)
    username=models.CharField(max_length=30,null=True)
    share_text=models.TextField()
