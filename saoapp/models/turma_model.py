# coding: utf-8
"""Model de turma"""

from __future__ import unicode_literals
from django.db import models


class TurmaModel(models.Model):
    """Classe de model de turma"""

    turma = models.CharField(max_length=45)
    ativo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.turma
