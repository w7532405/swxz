from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from .models import User
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def regist_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            sex=form.cleaned_data.get('sex')
            id_card=form.cleaned_data.get('id_card')
            user = User.objects.create_user(name=name, telephone=telephone, sex=sex, id_card=id_card,password=password)
            user.save()
            return redirect('user:regist_re')
        else:
            errors=[value[0] for value in form.get_errors().values()]
            errors=set(errors)
            return render(request, 'user/regist.html',{'errors':list(errors)})
    return render(request, 'user/regist.html')
def regist_view_re(request):
    return render(request,'user/regist_re.html')
def login_view(request):
    if request.session.get('_auth_user_id'):
        return redirect(reverse('detail:index'))
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                telephone = form.cleaned_data.get('telephone')
                password = form.cleaned_data.get('password')
                remember = form.cleaned_data.get('remember')
                user = authenticate(request, username=telephone, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        if remember:
                            request.session.set_expiry(None)
                        else:
                            request.session.set_expiry(0)
                        return redirect(reverse('detail:index'))
                    else:
                        return render(request, 'user/login.html', {'errors': '您的账号被冻结了'})
                else:
                    return render(request, 'user/login.html', {'errors': '手机号或密码错误'})
            else:
                print(form.get_errors())
                return render(request,'user/login.html',{'errors': '密码不能少于6个长度！'})
        else:
            return render(request, 'user/login.html')
def forget_view(request):
    return render(request, 'user/forget.html')
def logout_view(request):
    logout(request)
    return render(request,'user/logout.html')
@login_required(login_url='/user/login/')
def login_index(request):
    return render(request,'detail/index.html',{'user':request.user})