# coding: utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic.base import View

from saoapp.forms.disciplinaForm import DisciplinaForm
from saoapp.models import DisciplinaModel


class DisciplinaListarView(View):
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
    def get(self, request):
        form = DisciplinaForm()
        return render(request, 'disciplina/cadastrar.html', {'form': form})

    def post(self, request):
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('disciplina_listar')

class DisciplinaEditarView(View):
    def get(self, request, id=None):
        dc = DisciplinaModel.objects.get(id=id)
        form = DisciplinaForm(instance=dc)
        return render(request, 'disciplina/cadastrar.html', {'form': form})

    def post(self, request, id=None):
        dc = DisciplinaModel.objects.get(id=id)
        form = DisciplinaForm(data=request.POST, instance=dc)
        if form.is_valid():
            form.save()
        return redirect('disciplina_listar')