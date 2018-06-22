from django import forms
from apps.mascota.models import Mascota
class MascotaForm(forms.ModelForm):

    class Meta:
        model= Mascota
        fields= [
            'nombre',
            'sexo',
            'edad',
            'peso',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels={
            'nombre':'nombre',
            'sexo':'sexo',
            'edad':'edad',
            'peso':'peso',
            'fecha_rescate':'fecha_rescate',
            'persona':'persona',
            'vacuna':'vacuna',
        }
        widgets= {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'peso': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
