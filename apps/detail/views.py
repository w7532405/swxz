from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url='/user/login/')
def index(request):
    return render(request,'detail/index.html',{'user':request.user})