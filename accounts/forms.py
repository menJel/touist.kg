from django import forms
from django.contrib.auth.models import User

#есть два вида форм 
# ModelForm  формы основанные на полях модели , и она может повлиять на базу 
# Form  форма созданная не на основа , обычна форма , неможет повлиять на базу

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data #leaned_data -берет и пока не отаправляет в базу , пока мы не проверим правильность 
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']