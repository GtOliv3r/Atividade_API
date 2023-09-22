from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.tarefa import Tarefa
from api.serializers.tarefaSerializer import TarefaSerializer
from api.models.aluno import Aluno
from django.http import Http404

class TarefasAlunoView(APIView):
    """
    Lista todas as tarefas de um aluno específico.
    """

    def get_aluno(self, aluno_id):
        try:
            return Aluno.objects.get(pk=aluno_id)  #
        except Aluno.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        aluno = self.get_aluno(pk)  # Alteração: Usando o método get_aluno para obter o objeto do aluno
        tarefas = Tarefa.objects.filter(aluno=aluno)  # Alteração: Filtrando as tarefas pelo aluno
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)