from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Login',

        })
        self.fields['email'].widget.attrs.update({
            'placeholder': '@amazon.com'
        })
        
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',            
            'email',            
            'password1',
            'password2'
        ]
