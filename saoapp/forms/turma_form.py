# coding: utf-8
"""Formulário de turma"""

from __future__ import unicode_literals
from django import forms
from saoapp.models import TurmaModel


class TurmaForm(forms.ModelForm):
    """Classe de formulário de turma"""

    turma = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'maxlength': 45, 'placeholder': 'Turma'}
        )
    )

    class Meta:
        """Classe de metadados"""
        model = TurmaModel
        exclude = ('ativo',)
