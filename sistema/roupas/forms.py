from django.forms import ModelForm
from roupas.models import Roupa

class FormularioRoupa(ModelForm):
    class Meta:
        model = Roupa
        exclude = []
    