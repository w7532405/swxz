from django.db import models

# Create your models here.
# user = User.objects.get(pk=190)
# # user3=User.objects.get(id=1)
# # user=User.objects.get(pk=2)
# wx = wx_id(openid='123', wx_pho='456')
# wx.category = user
# wx.save()
# user.save()
class WX_user(models.Model):
    open_id=models.CharField(max_length=30,unique=True)
    pho_url=models.TextField(null=True)
    user=models.ForeignKey('user.User',on_delete=models.CASCADE)
class Wx_Dayshare_Table(models.Model):
    open_id=models.CharField(max_length=30)
    nick_name=models.CharField(max_length=30)
    share_text=models.TextField()
    pho_url=models.CharField(max_length=300)
    share_time=models.DateTimeField(auto_now_add=True)
