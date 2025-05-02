# forms.py
from django import forms
from .models import Profil
from portfolio.widgets import JenisKelaminWidget

class ProfilAdminForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'
        widgets = {
            'jenis_kelamin': JenisKelaminWidget,
        }
        labels = {
            'jenis_kelamin': 'Jenis Kelamin',
        }