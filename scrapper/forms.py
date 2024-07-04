from django import forms
from .models import ScrapperConfig

class ScrapperConfigForm(forms.ModelForm):
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required=True, label="Name")
    url = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required=True, label="Url")
    css_selector = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required=True, label="Css_selector")
    frequency = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}), required=True, label="Frequency")
    
    class Meta:
        model = ScrapperConfig
        fields = ("name", "url", "css_selector", "frequency")
