# coding: utf-8
"""View de aluno"""

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.aluno_form import AlunoForm
from saoapp.models.aluno_model import AlunoModel


class AlunoListarView(View):
    """Classe de view de listagem de alunos"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            aluno = AlunoModel.objects.all()
            paginator = Paginator(aluno, 5)
            page = request.GET.get('page')
            try:
                dados = paginator.page(page)
            except PageNotAnInteger:
                dados = paginator.page(1)
            except EmptyPage:
                dados = paginator.page(paginator.num_pages)
            return render(request, 'aluno/listar.html', {'dados': dados})
        return redirect('index')

class AlunoCadastrarView(View):
    """Classe de view de cadastro de aluno"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            form = AlunoForm()
            return render(request, 'aluno/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        """Método POST"""

        if request.user.is_superuser:
            form = AlunoForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('aluno_listar')
        return redirect('index')

class AlunoEditarView(View):
    """Classe de view de edição de aluno"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, aluno_id=None):
        """Método GET"""

        if request.user.is_superuser:
            aluno = AlunoModel.objects.get(id=aluno_id)
            form = AlunoForm(instance=aluno)
            return render(request, 'aluno/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, aluno_id=None):
        """Método POST"""

        if request.user.is_superuser:
            aluno = AlunoModel.objects.get(id=aluno_id)
            form = AlunoForm(data=request.POST, instance=aluno)
            if form.is_valid():
                form.save()
            return redirect('aluno_listar')
        return redirect('index')

class AlunoOcultarView(View):
    """Classe de view de ocultação de aluno"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, aluno_id=None):
        """Método GET"""

        if request.user.is_superuser:
            aluno = AlunoModel.objects.get(id=aluno_id)
            if aluno.ativo:
                aluno.ativo = False
            else:
                aluno.ativo = True
            aluno.save()
            return redirect('aluno_listar')
        return redirect('index')
