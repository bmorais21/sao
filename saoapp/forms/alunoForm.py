# coding: utf-8

from django import forms
from saoapp.models import AlunoModel, TurmaModel

class AlunoForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'Nome'}
        )
    )

    sobrenome = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'Sobrenome'}
        )
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'E-Mail'}
        )
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'Telefone (apenas números)'}
        )
    )

    matricula = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 6, 'min_value': 0, 'placeholder': 'Matrícula'}
        )
    )

    turma = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown'}
        ),
        queryset=TurmaModel.objects.all(),
        empty_label="Selecione uma turma"
    )

    class Meta:
        model = AlunoModel
        fields = "__all__"