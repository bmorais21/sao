# coding: utf-8

from django.db import models
from turmaModel import TurmaModel

class AlunoModel(models.Model):
    matricula = models.PositiveIntegerField(primary_key=True, max_length=6)
    nome = models.CharField(max_length=45)
    sobrenome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefone = models.IntegerField(max_length=11)
    turma = models.ForeignKey(TurmaModel)

    def __unicode__(self):
        return self.nome