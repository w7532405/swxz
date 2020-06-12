from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import WX_user
from apps.user.models import User
from django.http import JsonResponse
from apps.zjyq.models import DayText
from datetime import datetime
from apps.wxapi.models import Wx_Dayshare_Table
from apps.advise.models import Advise
from apps.passper.models import PassPer
import requests,json
# Create your views here.
class get_WXID(APIView):
    def post(self, request, *args, **kwargs):
        name = ''
        is_super = False
        pho_url = request.data.get('pho_url')
        wx_openid = request.data.get('wx_openid')
        if WX_user.objects.filter(open_id=wx_openid):
            pk = WX_user.objects.get(open_id=wx_openid).user_id
            name = User.objects.get(pk=pk).name
            is_super = User.objects.get(pk=pk).is_superuser
            wx_user = WX_user.objects.get(user_id=pk)
            wx_user.pho_url = pho_url
            wx_user.save()
            regist = True
        else:
            regist = False
        return JsonResponse({'status': True, 'regist': regist, 'realName': name, 'is_super': is_super})

class Regist(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        telephone = request.data.get('telephone')
        id_card = request.data.get('id_card')
        sex = request.data.get('sex')
        password = request.data.get('password')
        open_id = request.data.get('open_id')
        regist_re = ''
        regist_detail = ''
        if User.objects.filter(telephone=telephone).exists():
            regist_re = 'failure'
            regist_detail = '该手机号已注册！'
        if User.objects.filter(id_card=id_card).exists():
            regist_re = 'failure'
            regist_detail = '该身份证号已注册！'
        if len(regist_re) == 0:
            user = User.objects.create_user(name=name, telephone=telephone, sex=sex, id_card=id_card, password=password)
            user.save()
            wx_user = WX_user(open_id=open_id)
            wx_user.user = user
            wx_user.save()
            # print(wx_user)
            regist_re = 'success'
            regist_detail = '恭喜你注册成功！'
        return JsonResponse({'status': True, 'regist_re': regist_re, 'regist_detail': regist_detail})

class Login(APIView):
    def post(self, request, *args, **kwargs):
        telephone = request.data.get('telephone')
        password = request.data.get('password')
        open_id = request.data.get('open_id')
        status = ''
        user = authenticate(request, username=telephone, password=password)
        if user:
            wx_user = WX_user(open_id=open_id)
            wx_user.user = user
            wx_user.save()
            status = 'success'
        else:
            status = 'failure'
        # if user:
        # 	wx_user = WX_user(open_id=open_id)
        # 	wx_user.user=user
        # 	wx_user.save
        #     status = True
        # else:
        #     status = False
        return JsonResponse({'status': True, 'login_re': status})

class User_detail(APIView):
    def post(self, request, *args, **kwargs):
        wx_openid = request.data.get('open_id')
        wx_user = WX_user.objects.get(open_id=wx_openid)
        user = wx_user.user
        return JsonResponse({'status': True, 'user': {'name': user.name, 'sex': user.sex, 'telephone': user.telephone,
                                                  'id_card': user.id_card, 'is_active': user.is_active}})

class Su_regist(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        telephone = request.data.get('telephone')
        id_card = request.data.get('id_card')
        sex = request.data.get('sex')
        password = request.data.get('password')
        if not password:
            password = "123456"
        regist_re = ''
        regist_detail = ''
        if User.objects.filter(telephone=telephone).exists():
            regist_re = 'failure'
            regist_detail = '该手机号已注册！'
        if User.objects.filter(id_card=id_card).exists():
            regist_re = 'failure'
            regist_detail = '该身份证号已注册！'
        if len(regist_re) == 0:
            user = User.objects.create_user(name=name, telephone=telephone, sex=sex, id_card=id_card, password=password)
            user.save()
            regist_re = 'success'
            regist_detail = '注册成功！'
        return JsonResponse({'status': True, 'regist_re': regist_re, 'regist_detail': regist_detail})

class Su_show(APIView):
    def post(self, request, *args, **kwargs):
        telephone = request.data.get('telephone')
        is_null = '1'
        detail = {}
        user = User.objects.filter(telephone=telephone)[0]
        if user:
            detail = {'name': user.name, 'sex': user.sex,
                      'telephone': user.telephone, 'id_card': user.id_card,
                      'is_active': user.is_active}
            is_null = '0'
        return JsonResponse({'status': True, 'is_null': is_null, 'detail': detail})

class Su_delete(APIView):
    def post(self, request, *args, **kwargs):
        telephone = request.data.get('telephone')
        user = User.objects.filter(telephone=telephone)
        if user:
            user.delete()
            have_user = '1'
        else:
            have_user = '0'
        return JsonResponse({'status': True, 'have_user': have_user})

class Su_change(APIView):
    def post(self, request, *args, **kwargs):
        telephone = request.data.get('telephone')
        user = User.objects.filter(telephone=telephone)[0]
        name = request.data.get('name')
        telephone1 = request.data.get('telephone1')
        id_card = request.data.get('id_card')
        sex = request.data.get('sex')
        is_active = request.data.get('is_active')
        print(name)
        print(telephone1)
        if name:
            user.name = name
        if telephone1:
            user.telephone = telephone1
        if id_card:
            user.id_card = id_card
        if sex:
            user.sex = sex
        if is_active:
            user.is_active = is_active
        user.save()
        return JsonResponse({'status': True})
class Wx_is_day(APIView):
    def post(self,request,*args,**kwargs):
        open_id = request.data.get('open_id')
        telephone = WX_user.objects.get(open_id=open_id).user.telephone
        if DayText.objects.filter(refer_time__year=datetime.now().year,
                                  refer_time__month=datetime.now().month,refer_time__day=datetime.now().day):
            is_day='1'
        else:
            is_day='0'
        return JsonResponse({'status':True,'telephone':telephone,'is_day':is_day})
class Wx_dayText(APIView):
    def post(self, request, *args, **kwargs):
        telephone = request.data.get('telephone')
        province = request.data.get('province')
        city = request.data.get('city')
        area = request.data.get('area')
        de_addr = request.data.get('de_addr')
        hot = request.data.get('hot')
        danger_area = request.data.get('danger_area')
        cough = request.data.get('cough')
        other_cases = request.data.get('other_cases')
        result='0'
        if province and city and area and de_addr and hot and danger_area and cough:
            user = User.objects.get(telephone=telephone)
            day_text = DayText(province=province, city=city, area=area,
                               de_addr=de_addr, hot=hot, danger_area=danger_area, cough=cough,
                               other_cases=other_cases)
            day_text.user=user
            day_text.save()
            result='1'
        return JsonResponse({'status':True,'result':result})
class Wx_getText(APIView):
    def post(self, request, *args, **kwargs):
        open_id = request.data.get('open_id')
        user = WX_user.objects.get(open_id=open_id).user
        all_data = DayText.objects.filter(user=user).order_by('-refer_time')[0:7]
        datas=[]
        for k in all_data:
            if k.hot:
                hot='是'
            else:
                hot='否'
            if k.danger_area:
                danger_area = '是'
            else:
                danger_area = '否'
            if k.cough:
                cough = '是'
            else:
                cough = '否'
            time=k.refer_time.strftime('%Y年%m月%d日 %M时%I分%S秒')
            datas.append({'time':time,'province':k.province,'city':k.city,'area':k.area,'de_addr':k.de_addr,
                          'hot':hot,'danger_area':danger_area,'cough':cough,'other_cases':k.other_cases})
        return JsonResponse({'status':True,'days_data':datas})
class Wx_qrcode(APIView):
    def post(self, request, *args, **kwargs):
        year=datetime.now().year
        month=datetime.now().month
        day=datetime.now().day
        open_id = request.data.get('open_id')
        user = WX_user.objects.get(open_id=open_id).user
        all_data = DayText.objects.filter(user=user)
        jilu = all_data.order_by("-refer_time")[0:7]
        if jilu[0].refer_time.year == year and jilu[0].refer_time.month == month and jilu[0].refer_time.day == day:
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
            status = '今日未打卡！！！！红色'
        return JsonResponse({'status':True,'qr_str':status})
class Wx_return(APIView):
    def get(self, request, *args, **kwargs):
        url="https://api.weixin.qq.com/sns/jscode2session?"+request.get_full_path().split('?')[1]
        text=requests.get(url).text
        a=json.loads(text)
        return JsonResponse(a)
class Wx_Dayshare(APIView):
    def get(self,request,*args,**kwargs):
        dayshares=Wx_Dayshare_Table.objects.order_by('share_time')
        text_n=[]
        for dayshare in dayshares:
            dict_a={}
            dict_a['open_id']=dayshare.open_id
            dict_a['nick_name']=dayshare.nick_name
            dict_a['share_text']=dayshare.share_text
            dict_a['pho_url']=dayshare.pho_url
            dict_a['share_time']=dayshare.share_time.strftime('%Y年-%m月-%d日 %H时%I分%S秒')
            text_n.append(dict_a)
        return JsonResponse({'status':True,'datas':text_n})
    def post(self,request,*args,**kwargs):
        open_id = request.data.get('open_id')
        nick_name = request.data.get('nick_name')
        share_text = request.data.get('share_text')
        pho_url = request.data.get('pho_url')
        dayshare=Wx_Dayshare_Table(open_id=open_id,nick_name=nick_name,share_text=share_text,pho_url=pho_url)
        dayshare.save()
        return JsonResponse({'status': True})
class Wx_Advise(APIView):
    def get(self,request,*args,**kwargs):
        advises = Advise.objects.order_by('advise_time')[0:10]
        list_a=[]
        for i in advises:
            dict_a={}
            dict_a['advise_username']=i.advise_username
            dict_a['advise_title']=i.advise_title
            dict_a['time']=i.advise_time.strftime('%Y年%m月%d日 %H时%I分%S秒')
            dict_a['text']=i.advise_text
            list_a.append(dict_a)
        return JsonResponse({'status':True,'datas':list_a})
    def post(self,request,*args,**kwargs):
        title=request.data.get('title')
        nick_name=request.data.get('nickname')
        text=request.data.get('text')
        Advise(advise_title=title,advise_username=nick_name,advise_text=text).save()
        return JsonResponse({'status':True})

class Wx_PassPer(APIView):
    def get(self,request,*args,**kwargs):
        open_id = request.GET.get('open_id')
        passpers=PassPer.objects.filter(sys_user_name=open_id)
        list_a=[]
        for passper in passpers:
            if passper.final_result==True:
                a='通过'
            else:
                a='不通过'
            list_a.append({'pass_name':passper.pass_name,'pass_address':passper.pass_address,
                           'user_name':passper.user_name,'user_starttime':passper.user_starttime,
                           'user_stoptime':passper.user_stoptime,'final_result':a})
        return JsonResponse({'status':True,'datas':list_a})
    def post(self,request,*args,**kwargs):
        pass_name = request.data.get('pass_name')
        pass_address = request.data.get('pass_address')
        user_name = request.data.get('user_name')
        user_starttime = request.data.get('user_starttime')
        user_stoptime = request.data.get('user_stoptime')
        open_id = request.data.get('open_id')
        passper=PassPer(pass_name=pass_name,pass_address=pass_address,user_name=user_name,
                            user_starttime=user_starttime,user_stoptime=user_stoptime,
                            sys_user_name=open_id)
        passper.save()
        return JsonResponse({'status':True})
class Wx_Check_PassPer(APIView):
    def get(self,request,*args,**kwargs):
        passpers=PassPer.objects.filter(final_result='0')
        list_a = []
        for passper in passpers:
            list_a.append({'pass_name': passper.pass_name, 'pass_address': passper.pass_address,
                           'user_name': passper.user_name, 'user_starttime': passper.user_starttime,
                           'user_stoptime': passper.user_stoptime,'final_result':'不通过'})
        return JsonResponse({'status': True, 'datas': list_a})
    def post(self,request,*args,**kwargs):
        pass_name = request.data.get('pass_name')
        open_id = request.data.get('open_id')
        passper=PassPer.objects.filter(pass_name=pass_name,sys_user_name=open_id)[0]
        passper.final_result=True
        passper.save()
        return JsonResponse({'status': True})