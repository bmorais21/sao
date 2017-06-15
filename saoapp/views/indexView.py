# coding: utf-8
import user

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View

class IndexView(View):
    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        return render(request, 'index.html')
