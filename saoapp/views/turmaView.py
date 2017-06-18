# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from saoapp.forms.turmaForm import TurmaForm
from saoapp.models.turmaModel import TurmaModel

class TurmaListarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        tr = TurmaModel.objects.all()
        paginator = Paginator(tr, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'turma/listar.html', {'dados': dados})

class TurmaCadastrarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        form = TurmaForm()
        return render(request, 'turma/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('turma_listar')

class TurmaEditarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        tr = TurmaModel.objects.get(id=id)
        form = TurmaForm(instance=tr)
        return render(request, 'turma/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, id=None):
        tr = TurmaModel.objects.get(id=id)
        form = TurmaForm(data=request.POST, instance=tr)
        if form.is_valid():
            form.save()
        return redirect('turma_listar')

class TurmaOcultarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        tr = TurmaModel.objects.get(id=id)
        if tr.ativo:
            tr.ativo = False
        else:
            tr.ativo = True
        tr.save()
        return redirect('turma_listar')