# coding: utf-8
"""View de index"""

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View


class IndexView(View):
    """Classe de view inicial"""

    @method_decorator(login_required(login_url='/login/'))
    def get(self, request):
        """Método GET"""

        return render(request, 'index.html')
