# coding: utf-8
"""Populate de disciplina"""

from __future__ import unicode_literals
import os
import django
import saoapp.models.disciplina_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')
django.setup()

#TODO: arrumar pouplates

def populate_disciplina():
    """Função de população de disciplina"""

    add_disicplina(disciplina="Programação I")
    add_disicplina(disciplina="Programação II")
    add_disicplina(disciplina="POO I")
    add_disicplina(disciplina="POO II")
    add_disicplina(disciplina="Redes I")
    add_disicplina(disciplina="Redes II")
    add_disicplina(disciplina="Serviço de Redes")


def add_disicplina(disciplina):
    """Função de criação de disciplina"""

    disciplina_model = saoapp.models.DisciplinaModel.objects.get_or_create(disciplina=disciplina, ativo=True)[0]
    disciplina_model.turma = disciplina
    disciplina_model.ativo = True
    disciplina_model.save()
    return disciplina_model


if __name__ == '__main__':
    print("Populando disciplina . . .")
    populate_disciplina()
    print("Disciplina populada com sucesso!")
