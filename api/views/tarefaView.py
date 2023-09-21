from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importando Modelo e Serializers
from api.models.tarefa import Tarefa
from api.serializers.tarefaSerializer import TarefaSerializer

class TarefaView(APIView):
    """
    Retrieve, update or delete a category instance.
    """


     # Método get para listar todos os alunos
    def get(self, request, format=None):
        alunos = Tarefa.objects.all()  # Chama todos os objetos do model Tarefa do banco de dados
        serializer = TarefaSerializer(alunos, many=True)  # Serializa as Tarefas
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna a lista serializada com mensagem de sucesso

    #Método Post
    def post(self, request, format=None): 
        serializer = TarefaSerializer(data=request.data) #Serializa o objeto json digitado 
        if (serializer.is_valid()): #Verifica se é válido esse objeto
            serializer.save() #Se sim, armazena no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) #E retorna essa mensagem de sucesso
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Senão, retorna essa de falha
