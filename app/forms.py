# encoding: utf-8
"""
@version: 1.0
@author: xiongwenqiang
@software: PyCharm
@file: forms.py
@time: 2018/6/4/004 17:20
"""
from django import forms
from django.contrib.auth.hashers import make_password

from app.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password']

    password1 = forms.CharField(max_length=128)

    def clean_password1(self):
        if len(self.cleaned_data['password']) < 8:
            raise forms.ValidationError('密码长度过短')
        elif self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('密码不一致')
        else:
            self.cleaned_data['password'] = make_password(self.cleaned_data['password'])


class LoginForm(forms.Form):
   name = forms.CharField(max_length=32,required=True)
   password = forms.CharField(max_length=128,required=True)