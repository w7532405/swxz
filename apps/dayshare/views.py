from django.shortcuts import render
from .models import DayShare
# Create your views here.
def show(request):
    datas=DayShare.objects.order_by('share_time')[0:10]
    return render(request,'detail/dayshare/show.html',{'datas':datas})
def write(request):
    if request.method=='GET':
        return render(request,'detail/dayshare/write.html')
    else:
        share_text=request.POST.get('share_text')
        day_share=DayShare(username=request.user.name,share_text=share_text)
        day_share.save()
        return render(request,'detail/dayshare/write.html',{'result':'添加成功！！！'})