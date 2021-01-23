from django import forms
from .validation import *

class PiedataForm(forms.Form):
    title = forms.CharField(min_length=3,max_length=50,strip=True,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter the title','class':'form-control'}),help_text='Title should have more than 3 characters',validators=[validate_title])







# column1 = forms.CharField(min_length=2,label='Heading of first column',max_length=150,strip=True,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter the first column heading','class':'form-control'}),help_text='Heading should not have less than 2 characters more than 150 characters')
# column2 = forms.CharField(min_length=2,label='Heading of second column',max_length=150,strip=True,required=True,widget=forms.TextInput(attrs={'placeholder':'Enter the second column heading','class':'form-control'}),help_text='Heading should not have less than 2 characters more than 150 characters')