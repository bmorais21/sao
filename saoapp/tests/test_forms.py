# coding=utf-8
"""Testes de formulário"""
from django.test import TestCase
from saoapp.forms.turma_form import TurmaForm
from saoapp.models.turma_model import TurmaModel


class TurmaFormTest(TestCase):
    """Classe de teste do formulário de aluno"""
    def test_valid_form(self):
        """Método de teste de validação"""

        turma = TurmaModel.objects.create(turma=u'BSI Teste')

        data = {'turma': turma.turma,}

        form = TurmaForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Método de teste de validação com resultado falso"""
        turma = TurmaModel.objects.create(turma=u'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

        data = {'turma': turma.turma, }

        form = TurmaForm(data=data)
        self.assertFalse(form.is_valid())
