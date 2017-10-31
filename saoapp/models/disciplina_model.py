# coding: utf-8
"""Model de disciplina"""

from __future__ import unicode_literals
from django.db import models


class DisciplinaModel(models.Model):
    """
    Classe de model de disciplina

    :param disciplina: models.CharField(max_length=45)
    :param ativo: models.BooleanField(default=True)
    """

    disciplina = models.CharField(max_length=45)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.disciplina
