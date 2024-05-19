from django import forms
from .models import Service, Tour



class Serviceform(forms.ModelForm):
    country=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    destination=forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"number"}))
    
    

    class Meta:
        model=Service
        fields=('country', 'destination', 'view', 'tour', 'image')              
