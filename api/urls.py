from django.urls import path
from api.views.alunoView import AlunoView
from api.views.alunoDetailView import AlunoDetailView
from api.views.disciplinaDetailView import DisciplinaDetailView
from api.views.disciplinaView import DisciplinaView
from api.views.tarefaAlunoView import TarefasAlunoView
from api.views.tarefaDetailView import TarefaDetailView
from api.views.tarefaView import TarefaView

api_urls = [
    path('alunos/', AlunoView.as_view()),
    path('alunos/<int:pk>/', AlunoDetailView.as_view()),
    path('disciplinas/', DisciplinaView.as_view()),
    path('disciplinas/<int:pk>/', DisciplinaDetailView.as_view()),
    path('tarefas/', TarefaView.as_view()),
    path('tarefas/<int:pk>/', TarefaDetailView.as_view()),
    path('alunos/<int:pk>/tarefas/', TarefasAlunoView.as_view()),
]
