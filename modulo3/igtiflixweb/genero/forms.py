from django import forms
from genero.models import Genero
class GeneroForm(forms.ModelForm):

    class Meta:  # nome padrão para classe de meta dados
        model = Genero
        fields = '__all__'  # campos a serem mostrados no formulário