from django.db import models

# Create your models here.

class DayText(models.Model):
    province=models.CharField(max_length=20)    #北京         内蒙古
    city=models.CharField(max_length=20)        #北京         锡林郭勒盟
    area=models.CharField(max_length=20)        #朝阳         二连浩特
    de_addr=models.CharField(max_length=20)     #南大街xxxx号
    hot=models.BooleanField()
    danger_area=models.BooleanField()
    cough=models.BooleanField()
    other_cases=models.CharField(max_length=20,null=True)
    refer_time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey('user.User',on_delete=models.CASCADE)