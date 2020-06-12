from django.db import models

# Create your models here.
class Advise(models.Model):
    advise_title=models.CharField(max_length=30)
    advise_username=models.CharField(max_length=30)
    advise_time=models.DateTimeField(auto_now_add=True)
    advise_text=models.TextField()