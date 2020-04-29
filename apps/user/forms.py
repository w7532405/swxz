from django import forms
from .models import User
class FormMixin(object):
    def get_errors(self):
        if hasattr(self, 'errors'):
            errors = self.errors.get_json_data()
            new_errors = {}
            for key, message_dicts in errors.items():
                messages = []
                for message in message_dicts:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}
class LoginForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, min_length=6,
                               error_messages={"max_length": "密码最多不能超过20个字符！", "min_length": "密码最少不能少于6个字符！"})
    remember = forms.IntegerField(required=False)
class RegisterForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11)
    name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, min_length=6,
                                error_messages={"max_length": "密码最多不能超过20个字符！", "min_length": "密码最少不能少于6个字符！"})
    password2 = forms.CharField(max_length=20, min_length=6,
                                error_messages={"max_length": "密码最多不能超过20个字符！", "min_length": "密码最少不能少于6个字符！"})
    sex = forms.CharField(max_length=11)
    id_card = forms.CharField(max_length=18, min_length=18,
                             error_messages={"max_length": "身份证最多不能超过18个字符！", "min_length": "身份证最少不能少于18个字符！"})
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        telephone = cleaned_data.get('telephone')
        id_card=cleaned_data.get('id_card')
        if password != password2:
            raise forms.ValidationError('两次密码输入不一致！')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError('该手机号码已经被注册！')
        exists = User.objects.filter(id_card=id_card).exists()
        if exists:
            raise forms.ValidationError('该身份证号已经被注册！')
        return cleaned_data
