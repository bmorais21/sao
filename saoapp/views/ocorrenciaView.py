# coding: utf-8
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic.base import View

from saoapp.forms.ocorrenciaForm import OcorrenciaForm
from saoapp.models import OcorrenciaModel


class OcorrenciaListarView(View):
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
    def get(self, request):
        form = OcorrenciaForm()
        return render(request, 'ocorrencia/cadastrar.html', {'form': form})

    def post(self, request):
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ocorrencia_listar')