# coding: utf-8

from django.db import models

class DisciplinaModel(models.Model):
    disciplina = models.CharField(max_length=45)

    def __unicode__(self):
        return self.disciplina