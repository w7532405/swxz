from django.shortcuts import render
from .models import PassPer
# Create your views here.
def show(request):
    datas=PassPer.objects.filter(sys_user_name=request.user.name)
    return render(request,'detail/passper/show.html',{'datas':datas})
def write(request):
    result=''
    if request.method=='POST':
        pass_name=request.POST.get('pass_name')
        pass_address=request.POST.get('pass_address')
        user_name=request.POST.get('user_name')
        user_starttime=request.POST.get('user_starttime')
        user_stoptime=request.POST.get('user_stoptime')
        img=request.FILES.get('img')
        result='您填写的数据有误！'
        if pass_name and pass_address and user_name and user_starttime and user_stoptime and img:
            passper=PassPer(pass_name=pass_name,pass_address=pass_address,user_name=user_name,
                            user_starttime=user_starttime,user_stoptime=user_stoptime,
                            img=img,sys_user_name=request.user.name)
            passper.save()
            result = '提交成功！请等待管理员审核'
    return render(request,'detail/passper/write.html',{'result':result})
def check(request):
    passpers=PassPer.objects.filter(final_result=0)
    fin=request.GET.get('fin')
    pk=request.GET.get('pk')
    if fin=="0" or fin=='1':
        a=PassPer.objects.get(pk=pk)
        a.final_result=fin
        a.save()
        # PassPer.objects.get(pk=request.GET.get('pk')).delete()
    return render(request,'detail/passper/check_passper.html',{'passpers':passpers})