from django import forms

class BuscaEspProfForm(forms.Form):
    buscaEspProf = forms.CharField(label='', widget=forms.TextInput(attrs=dict({'name':'palabra','class': 'form-control', 'type': 'text', 'placeholder': 'Ingresá un nombre o una especialidad', 'id': 'id_buscaEspProf'})))

