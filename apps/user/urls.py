from django.urls import path

from . import views
app_name='user'
urlpatterns=[
    path('regist/',views.regist_view,name='regist'),
    path('regist_re/',views.regist_view_re,name='regist_re'),
    path('login/',views.login_view,name='login'),
    path('forget/',views.forget_view,name='forget'),
    path('logout/',views.logout_view,name='logout'),
]