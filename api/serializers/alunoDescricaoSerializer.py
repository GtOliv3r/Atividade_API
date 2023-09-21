#Importação do necessário para funcionalidade do Serializer
from rest_framework import serializers
from api.models.aluno import Aluno

class AlunoEmailSerializer(serializers.ModelSerializer):
    class Meta: #Classe padrão 
        model = Aluno #Modelo que esta sendo serializado
        fields = ['id', 'email'] #Serializa os campos especificos do model Disciplina