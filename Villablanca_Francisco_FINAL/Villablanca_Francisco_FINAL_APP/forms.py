from django import forms
from .models import Inscrito, Institucion

class InscritoForm(forms.ModelForm):
    fecha_inscripcion = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'2023-12-12'}))
    hora_inscripcion = forms.TimeField(widget=forms.TextInput(attrs={'placeholder':'12:00'}))
    class Meta:
        model = Inscrito
        fields = '__all__'
    

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'