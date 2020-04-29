from django.urls import path,include
from . import views
app_name="detail"
urlpatterns=[
    path('',views.index,name='index'),
    path('suadmin/',include('apps.suadmin.urls'))
]
