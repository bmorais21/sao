# coding: utf-8
"""Model de professor"""

from django.contrib.auth.models import User

class ProfessorModel(User):
    """Classe de model de professor"""

    def __unicode__(self):
        return self.first_name
