# coding: utf-8
"""View de ocorrência"""

from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.ocorrencia_form import OcorrenciaForm
from saoapp.models import OcorrenciaModel

class OcorrenciaListarView(View):
    """Classe de view de listagem de ocorrências"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        if request.user.is_superuser:
            ocorrencia = OcorrenciaModel.objects.all()
        else:
            ocorrencia = OcorrenciaModel.objects.filter(ativo=True)
        paginator = Paginator(ocorrencia, 5)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'ocorrencia/listar.html', {'dados': dados})

class OcorrenciaCadastrarView(View):
    """Classe de view de cadastro de ocorrência"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        form = OcorrenciaForm()
        return render(request, 'ocorrencia/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        """Método POST"""

        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'ocorrencia/cadastrar.html', {'form': form})
        return redirect('ocorrencia_listar')

class OcorrenciaEditarView(View):
    """Classe de view de edição de ocorrência"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, ocorrencia_id=None):
        """Método GET"""

        ocorrencia = OcorrenciaModel.objects.get(id=ocorrencia_id)
        form = OcorrenciaForm(instance=ocorrencia)
        print ocorrencia.hora
        return render(request, 'ocorrencia/cadastrar.html', {'form': form, 'hora': ocorrencia.hora})

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request, ocorrencia_id=None):
        """Método POST"""

        ocorrencia = OcorrenciaModel.objects.get(id=ocorrencia_id)
        form = OcorrenciaForm(data=request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'ocorrencia/cadastrar.html', {'form': form})
        return redirect('ocorrencia_listar')

class OcorrenciaOcultarView(View):
    """Classe de view de ocultação de ocorrência"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, ocorrencia_id=None):
        """Método GET"""

        if request.user.is_superuser:
            ocorrencia = OcorrenciaModel.objects.get(id=ocorrencia_id)
            if ocorrencia.ativo:
                ocorrencia.ativo = False
            else:
                ocorrencia.ativo = True
            ocorrencia.save()
            return redirect('ocorrencia_listar')
        else:
            return redirect('index')

class OcorrenciaRelatorioView(View):
    """Classe de view de relatório de ocorrência"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, ocorrencia_id=None):
        """Método GET"""

        dado = OcorrenciaModel.objects.get(pk=ocorrencia_id)
        return render(request, 'ocorrencia/relatorio.html', {'dado': dado})
