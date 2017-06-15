# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.disciplinaForm import DisciplinaForm
from saoapp.models import DisciplinaModel


class DisciplinaListarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        dc = DisciplinaModel.objects.all()
        paginator = Paginator(dc, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'disciplina/listar.html', {'dados': dados})

class DisciplinaCadastrarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        form = DisciplinaForm()
        return render(request, 'disciplina/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('disciplina_listar')

class DisciplinaEditarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        dc = DisciplinaModel.objects.get(id=id)
        form = DisciplinaForm(instance=dc)
        return render(request, 'disciplina/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, id=None):
        dc = DisciplinaModel.objects.get(id=id)
        form = DisciplinaForm(data=request.POST, instance=dc)
        if form.is_valid():
            form.save()
        return redirect('disciplina_listar')

class DisciplinaOcultarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        dc = DisciplinaModel.objects.get(id=id)
        if dc.ativo:
            dc.ativo = False
        else:
            dc.ativo = True
        dc.save()
        return redirect('disciplina_listar')