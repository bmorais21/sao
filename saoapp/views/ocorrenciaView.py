# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.ocorrenciaForm import OcorrenciaForm
from saoapp.models import OcorrenciaModel, TurmaModel


class OcorrenciaListarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        oc = OcorrenciaModel.objects.all()
        paginator = Paginator(oc, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'ocorrencia/listar.html', {'dados': dados})

class OcorrenciaCadastrarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        form = OcorrenciaForm()
        return render(request, 'ocorrencia/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        form = OcorrenciaForm(request.POST)
        t = TurmaModel.objects.get(pk=request.POST['aluno'])
        form.turma_id = t.id
        print form.errors
        if form.is_valid():
            form.save()
        return redirect('ocorrencia_listar')

class OcorrenciaRelatorioView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        dado = OcorrenciaModel.objects.get(pk=id)
        return render(request, 'ocorrencia/relatorio.html', {'dado': dado})