from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, TaskSerializer
from .models import TasksModel
# Create your views here.

def home(request):
    return render(request, 'index.html')

def usuários(request):
    return render(request, 'usuários.html')

def task(request):
    return render(request, 'create.html')


class UsersView(APIView):
    def get(self, request):
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        usuario = User.objects.get(id=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TaskView(APIView):
    def get(self, request):
        task = TasksModel.objects.all().order_by('-status', 'date')
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusView(APIView):
    def patch(self, request, pk):
        try:
            tarefa = TasksModel.objects.get(pk=pk)
        except TasksModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if tarefa.status:
            tarefa.status = False
        else:
            tarefa.status = True
        
        tarefa.save()
        return Response(status=status.HTTP_200_OK)