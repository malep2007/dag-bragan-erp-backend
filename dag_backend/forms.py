from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)

class RegisterUserForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='first name')
    last_name = forms.CharField( max_length=50, required=True)
    username = forms.CharField(max_length=50)
    password = forms.CharField( max_length=50, required=True, widget=forms.PasswordInput)
    repeat_password = forms.CharField( max_length=50, required=True)
    email = forms.EmailField(required=False)

