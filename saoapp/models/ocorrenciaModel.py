# coding: utf-8

from django.db import models
from saoapp.models import ProfessorModel, AlunoModel, DisciplinaModel

class OcorrenciaModel(models.Model):
    descricao = models.CharField(max_length=150)
    data = models.DateField()
    hora = models.TimeField()
    aluno = models.ForeignKey(AlunoModel)
    professor = models.ForeignKey(ProfessorModel)
    disciplina = models.ForeignKey(DisciplinaModel)


