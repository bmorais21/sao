# coding: utf-8
"""Formulário de disciplina"""

from django import forms
from saoapp.models import DisciplinaModel


class DisciplinaForm(forms.ModelForm):
    """Classe de formulário de aluno"""

    disciplina = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'maxlength': 45, 'placeholder': 'Disciplina'}
        )
    )

    class Meta:
        """Classe de metadados"""
        model = DisciplinaModel
        exclude = ('ativo',)
