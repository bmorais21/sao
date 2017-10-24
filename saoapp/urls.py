"""URLs do saoapp"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from saoapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),

    url(r'^$', IndexView.as_view(), name='index'),

    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),

    url(r'^aluno/$', AlunoListarView.as_view(), name='aluno_listar'),
    url(r'^aluno/cadastrar/$', AlunoCadastrarView.as_view(), name='aluno_cadastrar'),
    url(r'^aluno/editar/(?P<id>\d+)/$', AlunoEditarView.as_view(), name='aluno_editar'),
    url(r'^aluno/ocultar/(?P<id>\d+)/$', AlunoOcultarView.as_view(), name='aluno_ocultar'),

    url(r'^ocorrencia/$', OcorrenciaListarView.as_view(), name='ocorrencia_listar'),
    url(r'^ocorrencia/cadastrar/$', OcorrenciaCadastrarView.as_view(), name='ocorrencia_cadastrar'),
    url(r'^ocorrencia/editar/(?P<id>\d+)/$', OcorrenciaEditarView.as_view(), name='ocorrencia_editar'),
    url(r'^ocorrencia/ocultar/(?P<id>\d+)/$', OcorrenciaOcultarView.as_view(), name='ocorrencia_ocultar'),
    url(r'^ocorrencia/relatorio/(?P<id>\d+)/$', OcorrenciaRelatorioView.as_view(), name='ocorrencia_relatorio'),

    url(r'^turma/$', TurmaListarView.as_view(), name='turma_listar'),
    url(r'^turma/cadastrar/$', TurmaCadastrarView.as_view(), name='turma_cadastrar'),
    url(r'^turma/editar/(?P<id>\d+)/$', TurmaEditarView.as_view(), name='turma_editar'),
    url(r'^turma/ocultar/(?P<id>\d+)/$', TurmaOcultarView.as_view(), name='turma_ocultar'),

    url(r'^disciplina/$', DisciplinaListarView.as_view(), name='disciplina_listar'),
    url(r'^disciplina/cadastrar/$', DisciplinaCadastrarView.as_view(), name='disciplina_cadastrar'),
    url(r'^disciplina/editar/(?P<id>\d+)/$', DisciplinaEditarView.as_view(), name='disciplina_editar'),
    url(r'^disciplina/ocultar/(?P<id>\d+)/$', DisciplinaOcultarView.as_view(), name='disciplina_ocultar'),

    url(r'^professor/$', ProfessorListarView.as_view(), name='professor_listar'),
    url(r'^professor/cadastrar/$', ProfessorCadastrarView.as_view(), name='professor_cadastrar'),
    url(r'^professor/editar/(?P<id>\d+)/$', ProfessorEditarView.as_view(), name='professor_editar'),
    url(r'^professor/ocultar/(?P<id>\d+)/$', ProfessorOcultarView.as_view(), name='professor_ocultar'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
