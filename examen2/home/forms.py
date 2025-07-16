from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título'}),
            'userId': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el ID de usuario'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input', 'label': '¿Completado?'}),
        }
