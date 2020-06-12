from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from apps.user.models import User
@login_required(login_url='/user/login/')
def index(request):
    return render(request,'detail/index.html',{'user':request.user})

def change_password(request):
    errors=[]
    if request.method=="POST":
        user=request.user
        password0=request.POST.get('password0')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if user.check_password(password0):
            if password1!=password2:
                errors.append('两次输入密码不相符！！')
            else:
                if len(password1)==0:
                    errors.append('输入修改之后的密码不能为空！')
                elif len(password1)<6:
                    errors.append('输入修改之后的密码不能少于6位！')
                if len(password2) ==0:
                    errors.append('再次输入修改之后的密码不能为空！')
                elif len(password2)<6:
                    errors.append('再次输入修改之后的密码不能少于6位！')
                if len(password1)>=6 and password1==password2:
                    user.set_password(password1)
                    user.save()
                    errors.append('修改成功!')
            print(errors)
            return render(request,'detail/chapw.html',{'errors':errors})
        else:
            errors.append('当前密码错误！')
            return render(request,'detail/chapw.html',{'errors':errors})
    else:
        return render(request,'detail/chapw.html')

def show(request):
    return render(request,'detail/show.html')