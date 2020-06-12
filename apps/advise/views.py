from django.shortcuts import render,redirect
from .models import Advise
# Create your views here.
def show(request):
    advises = Advise.objects.order_by('advise_time')[0:10]
    return render(request,'detail/advise/show.html',{'advises':advises})
def show_detail(request):
    id=request.GET.get('pk')
    advise = Advise.objects.get(pk=id)
    return render(request,'detail/advise/show_detail.html',{'data':advise})
def check_advise(request):
    result=''
    advises=''
    if request.method=='POST':
        title=request.POST.get('advise_title')
        text=request.POST.get('advise_text')
        if len(title)>0 and len(text)>0:
            advise=Advise(advise_title=title,advise_text=text,advise_username=request.user.name)
            advise.save()
            result='添加成功！！请点击下方刷新按钮来查看（切勿手动刷新浏览器）'
    else:
        advises=Advise.objects.order_by('advise_time')[0:10]
    return render(request, 'detail/advise/check_advise.html', {'result':result, 'advises':advises})
def cha_advise(request):
    data=''
    if request.method=='GET':
        id=request.GET.get('pk')
        data=Advise.objects.get(pk=id)
    else:
        id=request.GET.get('pk')
        title=request.POST.get('title_text')
        text=request.POST.get('text')
        advise=Advise.objects.get(pk=id)
        if len(title)>0:
            advise.advise_title=title
        if len(text)>0:
            advise.advise_text=text
        advise.save()
        return redirect('detail:advise:check_advise')
    return render(request, 'detail/advise/cha_advise.html', {'data':data})
def del_advise(request):
    id=request.GET.get('pk')
    advise=Advise.objects.get(pk=id)
    return render(request, 'detail/advise/del_advise.html', {'data':advise})
def del_advise_re(request):
    id=request.GET.get('pk')
    Advise.objects.get(pk=id).delete()
    return redirect('detail:advise:check_advise')