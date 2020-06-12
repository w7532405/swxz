from django.shortcuts import render
from apps.user.models import User
from apps.zjyq.models import DayText
from datetime import datetime
# Create your views here.
def show(request):
    nan_num=len(User.objects.filter(sex='1'))
    nv_num=len(User.objects.filter(sex='0'))

    return render(request,'detail/tongji/show.html',{
        'sex_num':{'nan':nan_num,'nv':nv_num}})
def zjyq_show(request):
    a=DayText.objects.filter(refer_time__year=datetime.now().year
                             ,refer_time__month=datetime.now().month,refer_time__day=datetime.now().day)
    b=User.objects.all()
    c=DayText.objects.filter(refer_time__year=datetime.now().year
                             ,refer_time__month=datetime.now().month,refer_time__day=datetime.now().day,
                             hot=0,danger_area=0,cough=0,other_cases='')
    list_health=[];list_sick=[];list_notdaka=[]
    for i in range(7):
        day=datetime.now().day-i
        health=DayText.objects.filter(refer_time__year=datetime.now().year
                             ,refer_time__month=datetime.now().month,refer_time__day=day,
                             hot=0,danger_area=0,cough=0,other_cases='')
        daka=DayText.objects.filter(refer_time__year=datetime.now().year
                             ,refer_time__month=datetime.now().month,refer_time__day=day)
        list_health.append(len(health))
        list_notdaka.append(len(b)-len(daka))
        list_sick.append(len(daka)-len(health))
    return render(request,'detail/tongji/zjyq_show.html',{
        'time': [str(datetime.now().month)+'-'+str(datetime.now().day-i)for i in range(7)],
        'daka':{'is':len(a),'is_not':(len(b)-len(a))},
        'health':{'is_health':len(c),'is_sick':(len(b)-(len(b)-len(a))-len(c))},
        'list_health':list_health,
        'list_sick':list_sick,
        'list_notdaka':list_notdaka
    })