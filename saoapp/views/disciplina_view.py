# coding: utf-8
"""View de disciplina"""

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic import ListView

from saoapp.forms.disciplina_form import DisciplinaForm
from saoapp.models import DisciplinaModel


class DisciplinaListarView(ListView):
    """Classe genérica de view de listagem de disciplinas"""

    template_name = 'disciplina/listar.html'
    paginate_by = 5

    def get_queryset(self):
        """Método de definição de queryset"""
        return DisciplinaModel.objects.all()



class DisciplinaCadastrarView(View):
    """Classe de view de cadastro de disciplina"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            form = DisciplinaForm()
            return render(request, 'disciplina/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        """Método POST"""

        if request.user.is_superuser:
            form = DisciplinaForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('disciplina_listar')
        return redirect('index')

class DisciplinaEditarView(View):
    """Classe de view de edição de disciplina"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, disciplina_id=None):
        """Método GET"""
        if request.user.is_superuser:
            disciplina = DisciplinaModel.objects.get(id=disciplina_id)
            form = DisciplinaForm(instance=disciplina)
            return render(request, 'disciplina/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, disciplina_id=None):
        """Método POST"""

        if request.user.is_superuser:
            disciplina = DisciplinaModel.objects.get(id=disciplina_id)
            form = DisciplinaForm(data=request.POST, instance=disciplina)
            if form.is_valid():
                form.save()
            return redirect('disciplina_listar')
        return redirect('index')

class DisciplinaOcultarView(View):
    """Classe de view de ocultação de disciplina"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, disciplina_id=None):
        """Método GET"""

        if request.user.is_superuser:
            disciplina = DisciplinaModel.objects.get(id=disciplina_id)
            if disciplina.ativo:
                disciplina.ativo = False
            else:
                disciplina.ativo = True
            disciplina.save()
            return redirect('disciplina_listar')
        return redirect('index')
