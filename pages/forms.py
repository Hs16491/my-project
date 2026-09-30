from django import forms
from .models import Login

class LoginForms(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        #fields = ['username', 'password']

#class LoginForms(forms.Form):
    #username = forms.CharField(max_length=100, disabled=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}), required=True)
    #password = forms.CharField(max_length=100, widget=forms.PasswordInput())