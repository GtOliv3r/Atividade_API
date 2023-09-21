from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importando Modelo e Serializers
from api.models.disciplina import Disciplina
from api.serializers.disciplinaSerializer import DisciplinaSerializer
from api.serializers.tarefaSerializer import TarefaSerializer

class DisciplinaView(APIView):
    """
    Retrieve, update or delete a category instance.
    """


    # Método get para listar todos os alunos
    def get(self, request, format=None):
        alunos = Disciplina.objects.all()  # Chama todos os objetos do model Disciplina do banco de dados
        serializer = DisciplinaSerializer(alunos, many=True)  # Serializa as disciplinas
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna a lista serializada com mensagem de sucesso

    #Método Post
    def post(self, request, format=None): 
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   