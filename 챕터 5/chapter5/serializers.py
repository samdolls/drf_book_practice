from rest_framework import serializers
from .models import *

class TodoSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('todo_id', 'title', 'complete', 'important')

class TodoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'

class TodoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')