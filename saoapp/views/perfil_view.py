# coding: utf-8
import user

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

class PerfilView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        return render(request, 'perfil.html')

    @method_decorator(login_required(login_url='/login/'))
    def post(self, request):
        nova_senha = request.POST['nova_senha']
        confirmar_nova_senha = request.POST['confirmar_nova_senha']
        if nova_senha == confirmar_nova_senha:
            user = User.objects.get(aluno_id=request.user.id)
            user.set_password(nova_senha)
            user.save()
            return render(request, 'perfil.html', {'ok': 'ok'})
        else:
            return render(request, 'perfil.html', {'erro': 'erro'})