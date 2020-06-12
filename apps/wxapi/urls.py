from django.urls import path
from . import views
app_name='api'
urlpatterns=[
    path('login/',views.Login.as_view(),name='login'),
    path('regist/',views.Regist.as_view(),name='regist'),
    path('getwxid/',views.get_WXID.as_view(),name='get_wxid'),
    path('detail/',views.User_detail.as_view(),name='get_detail'),
    path('su_regist/',views.Su_regist.as_view(),name='su_regist'),
    path('su_show/',views.Su_show.as_view(),name='su_show'),
    path('su_delete/',views.Su_delete.as_view(),name='su_delete'),
    path('su_change/',views.Su_change.as_view(),name='su_change'),
    path('wx_is_day/',views.Wx_is_day.as_view(),name='wx_is_day'),
    path('wx_daytext/',views.Wx_dayText.as_view(),name='wx_daytext'),
    path('wx_gettext/',views.Wx_getText.as_view(),name='wx_gettext'),
    path('wx_qrcode/',views.Wx_qrcode.as_view(),name='wx_qrcode'),
    path('wx_return/',views.Wx_return.as_view(),name='wx_return'),
    path('wx_dayshare/',views.Wx_Dayshare.as_view(),name='wx_share'),
    path('wx_advise/',views.Wx_Advise.as_view(),name='wx_advise'),
    path('wx_passper/',views.Wx_PassPer.as_view(),name='wx_passper'),
    path('wx_check_passper/',views.Wx_Check_PassPer.as_view(),name='wx_check_passper'),
]
