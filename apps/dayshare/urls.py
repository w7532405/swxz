from django.urls import path
from . import views
app_name='dayshare'
urlpatterns=[
    path('show',views.show,name='show'),
    path('write',views.write,name='write'),
]