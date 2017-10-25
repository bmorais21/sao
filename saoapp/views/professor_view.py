# coding: utf-8
"""View de professor"""

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.professor_form import ProfessorForm
from saoapp.models.professor_model import ProfessorModel


class ProfessorListarView(View):
    """Classe de view de listagem de professores"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            professor = ProfessorModel.objects.all()
            paginator = Paginator(professor, 5)
            page = request.GET.get('page')
            try:
                dados = paginator.page(page)
            except PageNotAnInteger:
                dados = paginator.page(1)
            except EmptyPage:
                dados = paginator.page(paginator.num_pages)
            return render(request, 'professor/listar.html', {'dados': dados})
        return redirect('index')


class ProfessorCadastrarView(View):
    """Classe de view de cadastro de professor"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            form = ProfessorForm()
            return render(request, 'professor/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        """Método POST"""

        if request.user.is_superuser:
            form = ProfessorForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('professor_listar')
        return redirect('index')

class ProfessorEditarView(View):
    """Classe de view de edição de professor"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, professor_id=None):
        """Método GET"""

        if request.user.is_superuser:
            professor = ProfessorModel.objects.get(pk=professor_id)
            form = ProfessorForm(instance=professor)
            return render(request, 'professor/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, professor_id=None):
        """Método POST"""

        if request.user.is_superuser:
            professor = ProfessorModel.objects.get(pk=professor_id)
            form = ProfessorForm(data=request.POST, instance=professor)
            if form.is_valid():
                form.save()
            return redirect('professor_listar')
        return redirect('index')

class ProfessorOcultarView(View):
    """Classe de view de ocultação de professor"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, professor_id=None):
        """Método GET"""

        if request.user.is_superuser:
            professor = ProfessorModel.objects.get(aluno_id=professor_id)
            if professor.is_active:
                professor.is_active = False
            else:
                professor.is_active = True
            professor.save()
            return redirect('professor_listar')
        return redirect('index')
