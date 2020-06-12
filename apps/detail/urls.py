from django.urls import path,include
from . import views
app_name="detail"
urlpatterns=[
    path('',views.index,name='index'),
    path('suadmin/',include('apps.suadmin.urls')),
    path('zjyq/',include('apps.zjyq.urls')),
    path('tongji/',include('apps.tongji.urls')),
    path('passper/',include('apps.passper.urls')),
    path('things/',include('apps.things.urls')),
    path('dayshare/',include('apps.dayshare.urls')),
    path('cal/',include('apps.cal.urls')),
    path('advise/',include('apps.advise.urls')),
    path('chapw/',views.change_password,name='cha_pw'),
    path('show/',views.show,name='show'),
]
