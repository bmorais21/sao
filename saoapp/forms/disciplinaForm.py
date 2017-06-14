# coding: utf-8

from django import forms
from saoapp.models import DisciplinaModel


class DisciplinaForm(forms.ModelForm):
    disciplina = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'Disciplina'}
        )
    )

    class Meta:
        model = DisciplinaModel
        fields = "__all__"