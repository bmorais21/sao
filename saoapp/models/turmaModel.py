# coding: utf-8

from django.db import models

class TurmaModel(models.Model):
    turma = models.CharField(max_length=45)

    def __unicode__(self):
        return self.turma