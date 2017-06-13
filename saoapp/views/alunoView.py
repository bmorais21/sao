# coding: utf-8

from django.shortcuts import render
from django.views.generic.base import View
from saoapp.forms.alunoForm import AlunoForm

class AlunoListarView(View):
    def get(self, request):
        return render(request, 'aluno/listar.html')


class AlunoCadastrarView(View):
    def get(self, request):
        form = AlunoForm()
        return render(request, 'aluno/cadastrar.html', {'form': form})
