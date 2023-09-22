from rest_framework.serializers import ValidationError
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importando Modelo e Serializers
from api.models.tarefa import Tarefa
from api.serializers.tarefaSerializer import TarefaSerializer

class TarefaView(APIView):
    """
    POST de Tarefa e GET da lista de Tarefa
    """


     # Método get para listar todos os alunos
    def get(self, request, format=None):
        alunos = Tarefa.objects.all()  # Chama todos os objetos do model Tarefa do banco de dados
        serializer = TarefaSerializer(alunos, many=True)  # Serializa as Tarefas
        return Response(serializer.data, status=status.HTTP_200_OK)  # Retorna a lista serializada com mensagem de sucesso

    #Método Post
    def post(self, request, format=None): 
        try:
            serializer = TarefaSerializer(data=request.data) #Serializa o objeto json digitado 
            serializer.is_valid(raise_exception=True) #Verifica se é válido esse objeto
            serializer.save() #Se sim, armazena no banco de dados
            return Response(serializer.data, status=status.HTTP_201_CREATED) #E retorna essa mensagem de sucesso
        except ValidationError as error: #Erro de validação, que retorna o erro 400, por exemplo. Falta por algum dos campos no objeto JSON 
            return Response({"error": error.__class__.__name__, "cause": error.args}, status=status.HTTP_400_BAD_REQUEST) #Mensagem de BadRequest 400
        except Exception as error: #Qualquer erro que eu não conheça
            return Response({"error": error.__class__.__name__, "cause": error.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) #Mensagem de Internal Server error 500