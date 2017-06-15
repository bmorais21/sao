# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.alunoForm import AlunoForm
from saoapp.models.alunoModel import AlunoModel


class AlunoListarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        al = AlunoModel.objects.all()
        paginator = Paginator(al, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'aluno/listar.html', {'dados': dados})


class AlunoCadastrarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        form = AlunoForm()
        return render(request, 'aluno/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('aluno_listar')

class AlunoEditarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        al = AlunoModel.objects.get(id=id)
        form = AlunoModel(instance=al)
        return render(request, 'aluno/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, id=None):
        al = AlunoModel.objects.get(id=id)
        form = AlunoModel(data=request.POST, instance=al)
        if form.is_valid():
            form.save()
        return redirect('aluno_listar')

class AlunoOcultarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        al = AlunoModel.objects.get(id=id)
        if al.ativo:
            al.ativo = False
        else:
            al.ativo = True
        al.save()
        return redirect('aluno_listar')