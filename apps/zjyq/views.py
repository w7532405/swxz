from django.shortcuts import render
from .models import DayText
from apps.user.models import User
from django.http import HttpResponse
from datetime import datetime


def daytext(request):
    errors = []
    if request.method == 'POST':
        if DayText.objects.filter(refer_time__year=datetime.now().year,
                                  refer_time__month=datetime.now().month, refer_time__day=datetime.now().day):
            errors.append('您今天已经打过卡了')
        else:
            province = request.POST.get('province')
            city = request.POST.get('city')
            area = request.POST.get('area')
            de_addr = request.POST.get('detail_address')
            hot = request.POST.get('hot')
            danger_area = request.POST.get('danger_area')
            cough = request.POST.get('cough')
            other_cases = request.POST.get('other_cases')
            if province and city and area and de_addr and hot and danger_area and cough:
                day_text = DayText(province=province, city=city, area=area,
                                   de_addr=de_addr, hot=hot, danger_area=danger_area, cough=cough,
                                   other_cases=other_cases)
                user = request.user
                day_text.user = user
                day_text.save()
                errors.append('打卡成功！')
            else:
                errors.append('请输入有效值！！')
        return render(request, 'detail/zjyq/daytext.html', {'errors': errors})
    else:
        if DayText.objects.filter(refer_time__year=datetime.now().year,
                                  refer_time__month=datetime.now().month, refer_time__day=datetime.now().day):
            errors.append('您今天已经打过卡了')
        return render(request, 'detail/zjyq/daytext.html', {'errors': errors})


def userqr(request):
    status = ''
    status_su = '后端正在抓紧研发ing~~~'
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    jilu = DayText.objects.order_by("-refer_time")[0:7]
    if jilu[0].refer_time.year == year and jilu[0].refer_time.month == month and jilu[0].refer_time.day == day:
        if len(jilu) >= 6:
            if jilu[6].refer_time.day == (day - 6):
                new = 0
                for i in jilu:
                    if i.hot or i.cough or i.danger_area or i.other_cases:
                        status = '七天内有疾病记录！！！红色'
                        break
                    else:
                        new += 1
                if new == 7:
                    status = '七天内良好！！！绿色'
            else:
                status = '最近七天中有缺卡记录！！！红色'
        else:
            status = '最近七天中有缺卡记录！！！红色'
    else:
        status = '今日未打卡！！！！红色'
    return render(request, 'detail/zjyq/userqr.html', {'status': status, 'status_su': status_su})


def showday(request):
    datas = []
    all_datas = DayText.objects.filter(user=request.user.id).order_by('-refer_time')[0:7]
    for k in all_datas:
        datas.append({'time': k.refer_time,
                      'province': k.province, 'city': k.city, 'area': k.area, 'de_addr': k.de_addr,
                      'hot': k.hot, 'danger_area': k.danger_area, 'cough': k.cough, 'other_cases': k.other_cases})
    return render(request, 'detail/zjyq/showday.html', {'datas': datas})
