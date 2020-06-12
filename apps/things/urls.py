from django.urls import path
from . import views
app_name='things'
urlpatterns=[
    path('show',views.show,name='show'),
    path('write',views.write,name='write'),
    path('check',views.check,name='check'),
]