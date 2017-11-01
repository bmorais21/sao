# coding: utf-8
"""Formulário de ocorrencia"""

from __future__ import unicode_literals
from django import forms
from saoapp.models import AlunoModel, OcorrenciaModel, ProfessorModel, DisciplinaModel


class OcorrenciaForm(forms.ModelForm):
    """Classe de formulário de disciplina"""

    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={'required': 'True', 'maxlength': 150, 'placeholder': 'Descrição'}
        )
    )

    data = forms.DateField(
        widget=forms.DateInput(
            attrs={'required': 'True', 'maxlength': 10, 'type': 'date', 'placeholder': 'Data (ex: 21/07/1998)'}
        )
    )
    hora = forms.TimeField(
        widget=forms.DateInput(
            attrs={'required': 'True', 'maxlength': 5, 'type': 'time', 'placeholder': 'Hora (ex: 11:30)'}
        )
    )

    aluno = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=AlunoModel.objects.filter(ativo=True),
        empty_label="Selecione um Aluno"
    )

    professor = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=ProfessorModel.objects.filter(is_active=True),
        empty_label="Selecione um Professor"
    )

    disciplina = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=DisciplinaModel.objects.filter(ativo=True),
        empty_label="Selecione uma turma"
    )

    class Meta:
        """Classe de metadados"""
        model = OcorrenciaModel
        exclude = ('ativo',)
