# widgets.py
from django_select2.forms import ModelSelect2Widget
from .models import JenisKelamin

class JenisKelaminWidget(ModelSelect2Widget):
    model = JenisKelamin
    search_fields = ['jenis_kelamin']  # field pencarian untuk select2
