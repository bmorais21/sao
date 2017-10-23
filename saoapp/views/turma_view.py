# coding: utf-8
"""View de turma"""

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from saoapp.forms.turma_form import TurmaForm
from saoapp.models.turma_model import TurmaModel

class TurmaListarView(View):
    """Classe de view de listagem de turmas"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            turma = TurmaModel.objects.all()
            paginator = Paginator(turma, 5)
            page = request.GET.get('page')
            try:
                dados = paginator.page(page)
            except PageNotAnInteger:
                dados = paginator.page(1)
            except EmptyPage:
                dados = paginator.page(paginator.num_pages)
            return render(request, 'turma/listar.html', {'dados': dados})
        return redirect('index')

class TurmaCadastrarView(View):
    """Classe de view de cadastro de turma"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            form = TurmaForm()
            return render(request, 'turma/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        """Método POST"""

        if request.user.is_superuser:
            form = TurmaForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('turma_listar')
        return redirect('index')

class TurmaEditarView(View):
    """Classe de view de edição de turma"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, turma_id=None):
        """Método GET"""

        if request.user.is_superuser:
            turma = TurmaModel.objects.get(id=turma_id)
            form = TurmaForm(instance=turma)
            return render(request, 'turma/cadastrar.html', {'form': form})
        return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, turma_id=None):
        """Método POST"""

        if request.user.is_superuser:
            turma = TurmaModel.objects.get(id=turma_id)
            form = TurmaForm(data=request.POST, instance=turma)
            if form.is_valid():
                form.save()
            return redirect('turma_listar')
        return redirect('index')

class TurmaOcultarView(View):
    """Classe de view de ocultação de turma"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, turma_id=None):
        """Método GET"""

        if request.user.is_superuser:
            turma = TurmaModel.objects.get(id=turma_id)
            if turma.ativo:
                turma.ativo = False
            else:
                turma.ativo = True
            turma.save()
            return redirect('turma_listar')
        return redirect('index')
