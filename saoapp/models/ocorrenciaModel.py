# coding: utf-8

from django.db import models
from professorModel import ProfessorModel
from alunoModel import AlunoModel
from turmaModel import TurmaModel
from disciplinaModel import DisciplinaModel

class OcorrenciaModel(models.Model):
    descricao = models.CharField(max_length=150)
    data = models.DateTimeField()
    aluno = models.ForeignKey(AlunoModel)
    professor = models.ForeignKey(ProfessorModel)
    turma = models.ForeignKey(TurmaModel)
    disciplina = models.ForeignKey(DisciplinaModel)

    def __unicode__(self):
        return "Ocorrência do aluno " + self.aluno.nome + " em " + str(self.data) + "."