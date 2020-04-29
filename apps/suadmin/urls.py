from django.urls import path
from . import views
app_name='superuser'
urlpatterns=[
    path('cre/',views.create_user,name='create'),
    path('cres/',views.create_users,name='creates'),
    path('cha/',views.change_user,name='change'),
    path('del/',views.create_user,name='delete'),
    # path('show/',views.show_user,name='show'),
    path('show/',views.UserListView.as_view(),name='show'),
]