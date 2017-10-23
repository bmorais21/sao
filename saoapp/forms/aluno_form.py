# coding: utf-8
"""Formulário de aluno"""

from django import forms
from saoapp.models import AlunoModel, TurmaModel


class AlunoForm(forms.ModelForm):
    """Classe de formulário de aluno"""

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '^[a-zA-Z-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]*$',
                   'title': 'Apenas letras.', 'maxlength': 45, 'placeholder': 'Nome'}
        )
    )

    sobrenome = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'pattern': '^[a-zA-Z-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\s]*$',
                   'title': 'Apenas letras.', 'maxlength': 45, 'placeholder': 'Sobrenome'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'required': 'True', 'maxlength': 45, 'placeholder': 'E-Mail'}
        )
    )

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'maxlength': 14, 'pattern': '^[0-9]+$',
                   'title': 'Apenas números', 'placeholder': 'Telefone (apenas números)'}
        )
    )

    matricula = forms.IntegerField(
        widget=forms.TextInput(
            attrs={'required': 'True', 'maxlength': 6, 'pattern': '^[0-9]+$',
                   'title': 'Apenas números', 'placeholder': 'Matrícula'}
        )
    )

    turma = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=TurmaModel.objects.filter(ativo=True),
        empty_label="Selecione uma turma"
    )

    class Meta:
        """Classe de metadados"""
        model = AlunoModel
        exclude = ('ativo',)
