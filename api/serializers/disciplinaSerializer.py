#Importação do necessário para funcionalidade do Serializer
from rest_framework import serializers
from api.models.disciplina import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta: #Classe padrão 
        model = Disciplina #Modelo que esta sendo serializado
        fields = '__all__' #Serializa todas os campos do model Disciplina