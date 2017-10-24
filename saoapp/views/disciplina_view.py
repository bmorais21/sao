# coding: utf-8
"""View de disciplina"""

from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic import ListView

from saoapp.forms.disciplina_form import DisciplinaForm
from saoapp.models import DisciplinaModel


# class DisciplinaListarView(View):
#     """Classe de view de listagem de disciplinas"""
#
#     @method_decorator(login_required(login_url='/login/'))
#     def get(self, request):
#         """Método GET"""
#
#         if request.user.is_superuser:
#             dc = DisciplinaModel.objects.all()
#             paginator = Paginator(dc, 5)
#             page = request.GET.get('page')
#             try:
#                 dados = paginator.page(page)
#             except PageNotAnInteger:
#                 dados = paginator.page(1)
#             except EmptyPage:
#                 dados = paginator.page(paginator.num_pages)
#             return render(request, 'disciplina/listar.html', {'dados': dados})
#         else:
#             return redirect('index')

class DisciplinaListarView(ListView):
    """Classe genérica de view de listagem de disciplinas"""

    # TODO: terminar generic view
    template_name = 'disciplina/listar.html'

    def get_queryset(self):
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