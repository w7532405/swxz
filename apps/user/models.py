from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, telephone, password, name, **kwargs):
        if not telephone:
            raise ValueError('必须传递电话号')
        if not password:
            raise ValueError('必须传递密码')
        if not name:
            raise ValueError('必须传递姓名')
        user = self.model(telephone=telephone, name=name, **kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_user(self, telephone, password, name, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone, password=password, name=name, **kwargs)
    def create_super_user(self, telephone, password, name, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, password=password, name=name, **kwargs)
class User(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    id_card = models.CharField(max_length=18, unique=True)
    sex = models.CharField(max_length=10)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
