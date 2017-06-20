# coding: utf-8

from django import forms
from saoapp.models import AlunoModel, OcorrenciaModel, ProfessorModel, DisciplinaModel


class OcorrenciaForm(forms.ModelForm):
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={'required': 'True', 'maxlength': 150, 'placeholder': 'Descrição'}
        )
    )

    data = forms.DateField(
        widget=forms.DateInput(
            attrs={'required': 'True', 'type': 'date'}
        )
    )
    hora = forms.TimeField(
        widget=forms.DateInput(
            attrs={'required': 'True', 'type': 'time'}
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
        model = OcorrenciaModel
        exclude = ('ativo',)