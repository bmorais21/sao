# coding: utf-8
"""Model de ocorrência"""

from __future__ import unicode_literals
from django.db import models
from saoapp.models import ProfessorModel, AlunoModel, DisciplinaModel


class OcorrenciaModel(models.Model):
    """
    Classe de model de ocorrência

    :param descricao: models.CharField(max_length=150)
    :param data: models.DateField()
    :param hora: models.TimeField()
    :param aluno: models.ForeignKey(AlunoModel)
    :param professor: models.ForeignKey(ProfessorModel)
    :param disciplina: models.ForeignKey(DisciplinaModel)
    :param ativo: models.BooleanField(default=True)

    """

    descricao = models.CharField(max_length=150)
    data = models.DateField()
    hora = models.TimeField()
    aluno = models.ForeignKey(AlunoModel)
    professor = models.ForeignKey(ProfessorModel)
    disciplina = models.ForeignKey(DisciplinaModel)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return "Ocorrência do aluno " + self.aluno + " em " + self.data
