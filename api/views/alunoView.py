from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importando Modelo e Serializers
from api.models.aluno import Aluno
from api.serializers.alunoSerializer import AlunoSerializer

class AlunoView(APIView):
    """
    List and Post aluno instance(s).
    """

    # Método get para listar todos os alunos
    def get(self, request, format=None):
        alunos = Aluno.objects.all()  # Chama todos os objetos do model Aluno do banco de dados
        serializer = AlunoSerializer(alunos, many=True)  # Serializa os alunos
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna a lista serializada

    #Método Post
    def post(self, request, format=None): 
        serializer = AlunoSerializer(data=request.data) #Serializa o objeto json digitado 
        if (serializer.is_valid()): #Verifica se é válido esse objeto
            serializer.save() #Se sim, armazena no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) #E retorna essa mensagem de sucesso
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Senão, retorna essa de falha
