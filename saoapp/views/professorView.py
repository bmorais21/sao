# coding: utf-8
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from saoapp.forms.professorForm import ProfessorForm
from saoapp.models.professorModel import ProfessorModel


class ProfessorListarView(View):
    @method_decorator(login_required(login_url='/login/'))
    # @user_passes_test(lambda u: u.is_superuser)
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
        return render(request, 'professor/listar.html', {'dados': dados})


class ProfessorCadastrarView(View):
    @method_decorator(login_required(login_url='/login/'))
    # @user_passes_test(lambda u: u.is_superuser)
    def get(self, request):
        form = ProfessorForm()
        return render(request, 'professor/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    # @user_passes_test(lambda u: u.is_superuser)
    def post(self, request):
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('professor_listar')

class ProfessorEditarView(View):
    @method_decorator(login_required(login_url='/login/'))
    # @user_passes_test(lambda u: u.is_superuser)
    def get(self, request, id=None):
        pf = ProfessorModel.objects.get(pk=id)
        form = ProfessorModel(instance=pf)
        return render(request, 'professor/cadastrar.html', {'form': form})

    @method_decorator(login_required(login_url='/login/'))
    # @user_passes_test(lambda u: u.is_superuser)
    def post(self, request, id=None):
        pf = ProfessorModel.objects.get(pk=id)
        form = ProfessorModel(data=request.POST, instance=pf)
        if form.is_valid():
            form.save()
        return redirect('professor_listar')

class ProfessorOcultarView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request, id=None):
        pr = ProfessorModel.objects.get(id=id)
        if pr.is_active:
            pr.is_active = False
        else:
            pr.is_active = True
        pr.save()
        return redirect('professor_listar')