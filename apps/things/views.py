from django.shortcuts import render
from .models import Thing
# Create your views here.
def show(request):
    datas=Thing.objects.filter(username=request.user.name)
    return render(request,'detail/things/show.html',{'datas':datas})
def write(request):
    result=''
    if request.method=='POST':
        title=request.POST.get('pass_name')
        text=request.POST.get('pass_address')
        username=request.user.name
        if title and text:
            Thing(title=title,text=text,username=username).save()
            result='提交成功!'
        else:
            result='提交失败！'
    return render(request,'detail/things/write.html',{'result':result})
def check(request):
    fin=request.GET.get('fin')
    pk=request.GET.get('pk')
    if fin=="0" or fin=='1':
        a=Thing.objects.get(pk=pk)
        a.status=fin
        a.save()
    datas=Thing.objects.filter(status=0)
    return render(request,'detail/things/check.html',{'datas':datas})