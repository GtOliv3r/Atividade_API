from django.db import models

# Create your models here.

class Disciplina(models.Model):

  # Campos: nome, descricao

  nome = models.CharField(max_length=100)
  descricao = models.TextField()
  
  def __str__(self) -> str:
    return "Disciplina [%i - %s]" % (self.id, self.nome)
    