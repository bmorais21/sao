# coding: utf-8
"""Model de professor"""

from __future__ import unicode_literals
from django.contrib.auth.models import User


class ProfessorModel(User):
    """Classe de model de professor que herda de User"""

    def __unicode__(self):
        return self.first_name
