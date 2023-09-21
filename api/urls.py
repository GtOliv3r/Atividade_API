from django.urls import path
from api.views.alunoView import AlunoView
from api.views.disciplinaView import DisciplinaView
from api.views.tarefaView import TarefaView

api_urls = [
    path('alunos/', AlunoView.as_view()),
    path('alunos/<int:pk>/', AlunoView.as_view()),
    path('disciplinas/', DisciplinaView.as_view()),
    path('disciplinas/<int:pk>/', DisciplinaView.as_view()),
    path('tarefas/', TarefaView.as_view()),
    path('tarefas/<int:pk>/', TarefaView.as_view()),
]
