# coding: utf-8
"""Populate de professor"""

from __future__ import unicode_literals
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')
django.setup()

import saoapp.models.professor_model

def populate_professor():
    """Função de população de professor"""

    add_professor(first_name="Marco André", last_name="Mendes", email="marco@email.com",
                  username="marco", password="marco")
    add_professor(first_name="Ivo Marcos", last_name="Riegel", email="ivo@email.com",
                  username="ivo", password="ivo")
    add_professor(first_name="Fabio Longo", last_name="de Moura", email="fabio@email.com",
                  username="fabio", password="fabio")
    add_professor(first_name="Eduardo", last_name="Silva", email="eduardo@email.com",
                  username="eduardo", password="eduardo")


def add_professor(first_name, last_name, email, username, password):
    """Função de criação de professor"""

    professor_model = saoapp.models.ProfessorModel.objects.get_or_create(first_name=first_name,
                                                                         last_name=last_name, email=email,
                                                                         username=username, password=password,
                                                                         is_active=True)[0]
    professor_model.first_name = first_name
    professor_model.last_name = last_name
    professor_model.email = email
    professor_model.username = username
    professor_model.set_password(password)
    professor_model.is_active = True
    professor_model.save()
    return professor_model


if __name__ == '__main__':
    print("Populando professor . . .")
    populate_professor()
    print("Professor populado com sucesso!")
