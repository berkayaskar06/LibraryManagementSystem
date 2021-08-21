from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
class loginForm(forms.Form):
    username = forms.CharField(max_length=200, label='Username')
    password = forms.CharField(max_length=200, label= 'Password', widget=forms.PasswordInput)

    def clean(self):
        username =self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('Username or Password Wrong Try Again!')
            return super(loginForm, self).clean()

class registerForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Username')
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Verificate Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password does not match!")
        return password2