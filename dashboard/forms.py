from django import forms
from .models import ArchivoCsv

class FormularioCsv(forms.Form):
    archivo = forms.ModelChoiceField(
        queryset=ArchivoCsv.objects.all(),
        label='Selecciona un archivo',
        empty_label='Selecciona un archivo',
    )

    tipodato = forms.ChoiceField(
        label="seleccione tipo de dato",
        choices=(
            ('discrim', 'discrim'),
            ('n', 'n'),
            ('rspP','rspP'),
            ('pBis','pBis'),
            ('lower','lower'),
            ('mid50', 'mid50'),
            ('mid75','mid75'),
            ('upper', 'upper'),
        )
    )
