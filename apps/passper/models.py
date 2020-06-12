from django.db import models

# Create your models here.
class PassPer(models.Model):
    pass_name=models.CharField(max_length=30)
    pass_address=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    user_starttime=models.CharField(max_length=30)
    user_stoptime=models.CharField(max_length=30)
    img=models.ImageField(upload_to='img_dir/',null=True)
    sys_user_name=models.CharField(max_length=30)
    final_result=models.BooleanField(default=False,null=True)