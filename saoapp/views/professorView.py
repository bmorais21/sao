# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

# from saoapp.forms.professorForm import ProfessorForm
from saoapp.models.professorModel import ProfessorModel


class ProfessorListarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        al = ProfessorModel.objects.all()
        paginator = Paginator(al, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'Professor/listar.html', {'dados': dados})


class ProfessorCadastrarView(View):
    def get(self, request):
        form = ProfessorForm()
        return render(request, 'Professor/cadastrar.html', {'form': form})

    def post(self, request):
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Professor_listar')

class ProfessorEditarView(View):
    def get(self, request, id=None):
        al = ProfessorModel.objects.get(id=id)
        form = ProfessorModel(instance=al)
        return render(request, 'Professor/cadastrar.html', {'form': form})

    def post(self, request, id=None):
        al = ProfessorModel.objects.get(id=id)
        form = ProfessorModel(data=request.POST, instance=al)
        if form.is_valid():
            form.save()
        return redirect('Professor_listar')