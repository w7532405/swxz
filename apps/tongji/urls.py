from . import views
from django.urls import path
app_name='tongji'
urlpatterns=[
    path('show/',views.show,name='show'),
    path('zjyqshow/',views.zjyq_show,name='zjyq_show'),
]