"""sao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from saoapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^painel/$', PainelView.as_view(), name='painel'),

    url(r'^aluno/$', AlunoListarView.as_view(), name='aluno_listar'),
    url(r'^aluno/cadastrar/$', AlunoCadastrarView.as_view(), name='aluno_cadastrar'),
    url(r'^aluno/editar/(?P<id>\d+)/$', AlunoEditarView.as_view(), name='aluno_editar'),

    url(r'^ocorrencia/$', OcorrenciaListarView.as_view(), name='ocorrencia_listar'),
    url(r'^ocorrencia/cadastrar/$', OcorrenciaCadastrarView.as_view(), name='ocorrencia_cadastrar'),

    url(r'^turma/$', TurmaListarView.as_view(), name='turma_listar'),
    url(r'^turma/cadastrar/$', TurmaCadastrarView.as_view(), name='turma_cadastrar'),
    url(r'^turma/editar/(?P<id>\d+)/$', TurmaEditarView.as_view(), name='turma_editar'),


    url(r'^disciplina/$', DisciplinaListarView.as_view(), name='disciplina_listar'),
    url(r'^disciplina/cadastrar/$', DisciplinaCadastrarView.as_view(), name='disciplina_cadastrar'),
    url(r'^disciplina/editar/(?P<id>\d+)/$', DisciplinaEditarView.as_view(), name='disciplina_editar'),

    url(r'^professor/$', ProfessorListarView.as_view(), name='professor_listar'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
