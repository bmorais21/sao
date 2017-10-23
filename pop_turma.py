# coding: utf-8
"""Populate de turma"""

import os
import django
import saoapp.models.turma_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')
django.setup()


def populate_turma():
    """Função de população de turma"""

    add_turma(turma="BSI 1")
    add_turma(turma="BSI 2")
    add_turma(turma="BSI 3")
    add_turma(turma="BSI 4")
    add_turma(turma="BSI 5")
    add_turma(turma="BSI 6")
    add_turma(turma="BSI 7")
    add_turma(turma="BSI 8")

def add_turma(turma):
    turma_model = saoapp.models.TurmaModel.objects.get_or_create(turma=turma, ativo=True)[0]
    turma_model.turma = turma
    turma_model.ativo = True

    turma_model.save()
    return turma_model

if __name__ == '__main__':
    print "Populando turma . . ."
    populate_turma()
    print "Turma populada com sucesso!"
