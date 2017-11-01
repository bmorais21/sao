# coding: utf-8
"""Populate de professor"""

from __future__ import unicode_literals
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sao.settings')
django.setup()

from django.contrib.auth.models import User


if __name__ == '__main__':
    print("Criando administrador . . .")
    admin, c = User.objects.get_or_create(username=u'admin',
                                                 is_superuser=True,
                                                 is_staff=True)
    admin.set_password(u'admin@admin')
    admin.save()
    print("Adminstrador criado com sucesso!")
