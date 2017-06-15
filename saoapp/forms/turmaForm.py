# coding: utf-8

from django import forms
from saoapp.models import TurmaModel

class TurmaForm(forms.ModelForm):
    turma = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'Turma'}
        )
    )

    class Meta:
        model = TurmaModel
        exclude = ('ativo',)