# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')

import django

django.setup()

import saoapp.models.professorModel

def populate():
    add_professor(first_name="Marco André", last_name="Mendes", email="marco@email.com", username="marco", password="marco")
    add_professor(first_name="Ivo Marcos", last_name="Riegel", email="ivo@email.com", username="ivo", password="ivo")
    add_professor(first_name="Fabio Longo", last_name="de Moura", email="fabio@email.com", username="fabio", password="fabio")
    add_professor(first_name="Eduardo", last_name="Silva", email="eduardo@email.com", username="eduardo", password="eduardo")

def add_professor(first_name, last_name, email, username, password):
    m = saoapp.models.ProfessorModel.objects.get_or_create(first_name=first_name, last_name=last_name, email=email, username=username, password=password, is_active=True)[0]
    m.first_name = first_name
    m.last_name = last_name
    m.email = email
    m.username = username
    m.set_password(password)
    m.is_active = True

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting professor population script...")
    populate()