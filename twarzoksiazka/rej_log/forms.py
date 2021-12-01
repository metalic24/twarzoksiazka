from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import fields

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    #sprawdzanie, czy email się nie powtarza 
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email =email)
        if qs.exists():
            raise forms.ValidationError("this email is in use")
        
        return email

