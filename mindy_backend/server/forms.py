from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(label="Password", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email address", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    pwd1 = forms.CharField(label="Password", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pwd2 = forms.CharField(label="Confirm password", max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
