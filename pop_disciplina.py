# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')

import django

django.setup()

import saoapp.models.disciplinaModel

def populate():
    add_disicplina(disciplina="Programação I")
    add_disicplina(disciplina="Programação II")
    add_disicplina(disciplina="POO I")
    add_disicplina(disciplina="POO II")
    add_disicplina(disciplina="Redes I")
    add_disicplina(disciplina="Redes II")
    add_disicplina(disciplina="Serviço de Redes")

def add_disicplina(disciplina):
    m = saoapp.models.DisciplinaModel.objects.get_or_create(disciplina=disciplina, ativo=True)[0]
    m.turma = disciplina
    m.ativo = True

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting disciplina population script...")
    populate()