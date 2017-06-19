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
        if request.user.is_superuser:
            dc = DisciplinaModel.objects.all()
            paginator = Paginator(dc, 5)
            page = request.GET.get('page')
            try:
                dados = paginator.page(page)
            except PageNotAnInteger:
                dados = paginator.page(1)
            except EmptyPage:
                dados = paginator.page(paginator.num_pages)
            return render(request, 'disciplina/listar.html', {'dados': dados})
        else:
            return redirect('index')

class DisciplinaCadastrarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        if request.user.is_superuser:
            form = DisciplinaForm()
            return render(request, 'disciplina/cadastrar.html', {'form': form})
        else:
            return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        if request.user.is_superuser:
            form = DisciplinaForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('disciplina_listar')
        else:
            return redirect('index')

class DisciplinaEditarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        if request.user.is_superuser:
            dc = DisciplinaModel.objects.get(id=id)
            form = DisciplinaForm(instance=dc)
            return render(request, 'disciplina/cadastrar.html', {'form': form})
        else:
            return redirect('index')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, id=None):
        if request.user.is_superuser:
            dc = DisciplinaModel.objects.get(id=id)
            form = DisciplinaForm(data=request.POST, instance=dc)
            if form.is_valid():
                form.save()
            return redirect('disciplina_listar')
        else:
            return redirect('index')

class DisciplinaOcultarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        if request.user.is_superuser:
            dc = DisciplinaModel.objects.get(id=id)
            if dc.ativo:
                dc.ativo = False
            else:
                dc.ativo = True
            dc.save()
            return redirect('disciplina_listar')
        else:
            return redirect('index')