from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name='passper'
urlpatterns=[
    path('show/',views.show,name='show'),
    path('write/',views.write,name='write'),
    path('check/',views.check,name='check'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)