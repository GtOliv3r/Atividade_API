#Importação do necessário para funcionalidade do Serializer
from rest_framework import serializers
from api.models.aluno import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta: #Classe padrão 
        model = Aluno #Modelo que esta sendo serializado
        fields = '__all__' #Serializa todas os campos do model Aluno