from __future__ import unicode_literals
from django.contrib import admin
from saoapp.models import *

# TODO: comentar aqui e a url
admin.site.register(TurmaModel)
admin.site.register(AlunoModel)
admin.site.register(DisciplinaModel)
admin.site.register(OcorrenciaModel)
admin.site.register(ProfessorModel)

