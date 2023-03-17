from django import forms
from .models import Drama


class DramaForm(forms.ModelForm):
    class Meta:
        model = Drama
        fields = ['name', 'desc', 'year', 'img']
