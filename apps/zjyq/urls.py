from django.urls import path
from . import views
app_name='zjyq'
urlpatterns=[
    path('daytext/',views.daytext,name='daytext'),
    path('userqr/',views.userqr,name='userqr'),
    path('showday/',views.showday,name='showday'),
]