from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importando Modelo e Serializers
from api.models.disciplina import Disciplina
from api.serializers.disciplinaSerializer import DisciplinaSerializer
from api.serializers.tarefaSerializer import TarefaSerializer

class DisciplinaDetailView(APIView):
    """
    Retrieve, update or delete a discipline instance.
    """


    #Método Get para achar o objeto e ver se ele existe, utilizado em outros Metodos   
    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk) #tras o objeto usando id especifico
        except Disciplina.DoesNotExist: #Senão achar, mostra a mensagem dizendo que não existe esse objeto
            raise Http404 #Tela HTML de bad request
    
    
    #Método get especifico pelo id
    def get(self, request, pk, format=None):
        categoria = self.get_object(pk) #Chama o próprio método get_object e tras o objeto usando id especifico
        serializer = DisciplinaSerializer(categoria) # Desserializa o objeto do model disciplina e armazena em serializer
        return Response(serializer.data, status=status.HTTP_200_OK)  # Mensagem de sucesso

    #Método put
    def put(self, request, pk, format=None):
        categoria = self.get_object(pk) #Chama o próprio método get_object e tras o objeto usando id especifico
        serializer = DisciplinaSerializer(categoria,data=request.data) # Desserializa o objeto do model disciplina retornando os campos e armazena em serializer
        if (serializer.is_valid()): #Se as alterações estiverem corretas dentro do esperado, realiza a instrução abaixo
            serializer.save() #Salva no banco de Dados e mostra a mensagem abaixo de sucesso
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Mensagem de operação sucedida  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Senão mostra essa mensagem de operação falha
    
    #Método delete
    def delete(self, request, pk, format=None): 
        categoria = self.get_object(pk) #Chama o próprio método get_object e tras o objeto usando id especifico
        categoria.delete() #Deleta o objeto especificado pelo id
        return Response(status=status.HTTP_204_NO_CONTENT) #Retorna mensagem de sucesso nos dizendo que não mais conteúdo
    
    