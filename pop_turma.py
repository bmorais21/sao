# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')

import django

django.setup()

import saoapp.models.turmaModel


def populate():

    add_turma(turma="BSI 1")
    add_turma(turma="BSI 2")
    add_turma(turma="BSI 3")
    add_turma(turma="BSI 4")
    add_turma(turma="BSI 5")
    add_turma(turma="BSI 6")
    add_turma(turma="BSI 7")
    add_turma(turma="BSI 8")

def add_turma(turma):
    m = saoapp.models.TurmaModel.objects.get_or_create(turma=turma, ativo=True)[0]
    m.turma = turma
    m.ativo = True

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting turma population script...")
    populate()