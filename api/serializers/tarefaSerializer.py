#Importação do necessário para funcionalidade do Serializer
from rest_framework import serializers
from api.models.tarefa import Tarefa
from api.models.aluno import Aluno
from api.models.disciplina import Disciplina

from api.serializers.disciplinaSerializer import DisciplinaSerializer
from api.serializers.alunoSerializer import AlunoSerializer


class TarefaSerializer(serializers.ModelSerializer):
    aluno = serializers.PrimaryKeyRelatedField(queryset=Aluno.objects.all())  #campo de relacionamento
    disciplinas = serializers.PrimaryKeyRelatedField(many=True, queryset=Disciplina.objects.all())  #campo de relacionamento
    
    class Meta: #Classe padrão 
        model = Tarefa #Modelo que esta sendo serializado
        fields = '__all__' #Serializa todas os campos do model Aluno