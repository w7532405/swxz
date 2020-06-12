from django.urls import path
from . import views
app_name='advise'
urlpatterns=[
    path('show/',views.show,name='show'),
    path('show_detail/',views.show_detail,name='show_detail'),
    path('check_advise/', views.check_advise, name='check_advise'),
    path('cha_advise/', views.cha_advise, name='cha_advise'),
    path('del_advise/', views.del_advise, name='del_advise'),
    path('del_advise_re/', views.del_advise_re, name='del_advise_re'),
]