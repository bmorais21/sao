# coding: utf-8
import user

from django.shortcuts import render
from django.views.generic.base import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    # def post(self, request):
    #     form = UsuarioForm(request.POST)
    #     if request.POST['password'] == request.POST['senha_conferir']:
    #         if form.is_valid():
    #             form.save()
    #             user = User.objects.get(username=request.POST['username'])
    #             user.save()
    #             return render(request, 'index.html', {'cadastro': True, 'form': UsuarioForm()})
    #         else:
    #             return render(request, 'index.html', {'form': form, 'erro_cad': True})
    #     else:
    #         return render(request, 'index.html', {'form': form, 'senha_erro': True, 'erro_cad': True})