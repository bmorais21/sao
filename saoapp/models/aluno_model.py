# coding: utf-8
"""Model de aluno"""

from django.db import models
from saoapp.models.turma_model import TurmaModel


class AlunoModel(models.Model):
    """Classe de model de aluno"""

    matricula = models.BigIntegerField(unique=True)
    nome = models.CharField(max_length=45)
    sobrenome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefone = models.IntegerField()
    turma = models.ForeignKey(TurmaModel)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nome
