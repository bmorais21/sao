# coding: utf-8

from django.shortcuts import render
from django.views.generic.base import View

class TurmaListarView(View):
    def get(self, request):
        return render(request, 'turma/listar.html')