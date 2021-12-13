from django import forms
from django.db.models import fields
from .models import GWFUser

class NewUserForm(forms.ModelForm):
    class Meta:
        model = GWFUser
        fields = [
            'name',
            'login',
            'email',
            'password'
        ]