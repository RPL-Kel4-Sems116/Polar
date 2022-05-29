from urllib import request
from django import forms
from django.forms import ModelForm
from .models import Customer
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper

class orderForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'description',
            'email',
            'phone_number',
            'services',
        ]

        
        widgets = {
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number':forms.TextInput(attrs={'class': 'form-control'}),
            'services':forms.Select(attrs={'class': 'form-control'}),
        }

class searchForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'description',
        ]

        widgets = {
            'description':forms.TextInput(attrs={'placeholder': 'description',
                                                'class' : 'form-control'}),
        }

class UserCreateForm(UserCreationForm):
#   bambang = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
#    def save(self, commit=True):
#        user = super(UserCreateForm, self).save(commit=False)
#        user.bambang = self.cleaned_data["bambang"]
#        if commit:
#            user.save()
#        return user
    
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        for field in UserCreateForm.Meta.fields:
            self.fields[field].help_text = False