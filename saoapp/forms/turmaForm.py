# coding: utf-8

from django import forms
from saoapp.models import TurmaModel

class TurmaForm(forms.ModelForm):
    turma = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'Turma'}
        )
    )

    def save(self, commit=True):
        agente = super(TurmaForm, self).save(commit=False)
        if commit:
            agente.save()
        return agente

    class Meta:
        model = TurmaModel
        fields = "__all__"