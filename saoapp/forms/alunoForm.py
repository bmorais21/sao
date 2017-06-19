# coding: utf-8

from django import forms
from saoapp.models import AlunoModel, TurmaModel


class AlunoForm(forms.ModelForm):
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
        widget=forms.EmailInput(
            attrs={'required': 'True', 'max_length': 45, 'placeholder': 'E-Mail'}
        )
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 14, 'pattern': '^[0-9]+$', 'title': 'Apenas números', 'placeholder': 'Telefone (apenas números)'}
        )
    )

    matricula = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'max_length': 6, 'pattern': '^[0-9]+$', 'title': 'Apenas números', 'placeholder': 'Matrícula'}
        )
    )

    turma = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=TurmaModel.objects.all(),
        empty_label="Selecione uma turma"
    )

    class Meta:
        model = AlunoModel
        exclude = ('ativo',)