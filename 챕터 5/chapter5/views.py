from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
class TodosAPIView(APIView):
    
    def get(self,request):
        todos = Todo.objects.all()
        serializer = TodoSimpleSerializer(todos, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
        return Response(serializer.data)
    
class TodoAPIView(APIView):

    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, pk = todo_id)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data)
    
    def patch(self, request, todo_id):
        todo = get_object_or_404(Todo, pk = todo_id)
        serializer = TodoCreateSerializer(instance = todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, todo_id):
        todo = get_object_or_404(Todo, pk = todo_id)
        todo.delete()
        data = {
            'deleted_todo' : todo_id,
        }
        return Response(data)
    
class DoneTodosAPIView(APIView):

    def get(self, request):
        dones = Todo.objects.filter(complete = True)
        serializer = TodoSimpleSerializer(dones, many = True)
        return Response(serializer.data)
    
class DoneTodoAPIView(APIView):

    def get(self, request, todo_id):
        done = get_object_or_404(Todo, pk = todo_id)
        done.complete = True
        done.save()
        serializer = TodoDetailSerializer(done)
        return Response(serializer.data)