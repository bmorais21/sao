# coding: utf-8

from django.contrib.auth.models import User

class ProfessorModel(User):

    def __unicode__(self):
        return self.first_name