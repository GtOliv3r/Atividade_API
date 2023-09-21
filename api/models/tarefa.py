from django.db import models
from api.models.disciplina import Disciplina
from api.models.aluno import Aluno

# Create your models here.

class Tarefa(models.Model):

  # Campos: titulo, descricao, data_entrega, concluida


  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  data_entrega = models.DateField()
  status_conclusao = models.BooleanField(default=False)
  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)  # Relacionamento Um para N com Aluno
  disciplinas = models.ManyToManyField(Disciplina)  # Relacionamento N para N com Disciplina
  
  def __str__(self) -> str:
    return "Tarefa [%i - %s]" % (self.id, self.titulo)
    