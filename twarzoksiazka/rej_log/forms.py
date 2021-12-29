
from django.forms.widgets import DateInput, SelectDateWidget
from .models import  User_details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import fields



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email =email)
        if qs.exists():
            raise forms.ValidationError("this email is in use")
        
        return email

#liczy daty, bo domyślnie jest od bierzącego roku + 10 lat  
YEARS= [x for x in range(1940,2023)]

class CreateUserDetailsForm(forms.ModelForm):
    class Meta:
        model = User_details
        fields = ['name', 'surr_name', 'birth_date', 'bio']
        widgets = {
            'birth_date': SelectDateWidget(years=YEARS)
        }
        

