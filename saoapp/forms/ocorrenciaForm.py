# coding: utf-8

from django import forms
from saoapp.models import AlunoModel, OcorrenciaModel, ProfessorModel, DisciplinaModel


class OcorrenciaForm(forms.ModelForm):
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={'required': 'True', 'max_length': 150, 'placeholder': 'Descrição'}
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
        queryset=AlunoModel.objects.all(),
        empty_label="Selecione um Aluno"
    )

    professor = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=ProfessorModel.objects.all(),
        empty_label="Selecione uma turma"
    )

    disciplina = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'class': 'ui fluid dropdown', 'required': 'True'}
        ),
        queryset=DisciplinaModel.objects.all(),
        empty_label="Selecione uma turma"
    )

    class Meta:
        model = OcorrenciaModel
        fields = "__all__"