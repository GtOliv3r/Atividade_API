#Importação do necessário para funcionalidade do Serializer
from rest_framework import serializers
from api.models.tarefa import Tarefa
from api.serializers.disciplinaSerializer import DisciplinaSerializer
from api.serializers.alunoSerializer import AlunoSerializer


class TarefaSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer()  #campo de relacionamento
    disciplinas = DisciplinaSerializer(many=True)  #campo de relacionamento
    class Meta: #Classe padrão 
        model = Tarefa #Modelo que esta sendo serializado
        fields = '__all__' #Serializa todas os campos do model Aluno