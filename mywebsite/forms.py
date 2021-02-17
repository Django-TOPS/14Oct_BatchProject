from django import forms
from .models import signup,uploadpost


class signupForm(forms.ModelForm):
    class Meta:
        model=signup
        #fields=['fname','lanme']
        fields='__all__'

class uploadpostForm(forms.ModelForm):
    class Meta:
        model=uploadpost
        fields='__all__'


