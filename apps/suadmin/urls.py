from django.urls import path
from . import views
app_name='superuser'
urlpatterns=[
    path('cre/',views.create_user,name='create'),
    path('cres/',views.create_users,name='creates'),
    path('cres_re/',views.create_users_re,name='creates_re'),
    path('cha/',views.change_user,name='change'),
    path('del/', views.delete_user, name='delete'),
    path('delre/', views.delete_user_re, name='delete_re'),
    path('show/',views.UserListView.as_view(),name='show'),
]