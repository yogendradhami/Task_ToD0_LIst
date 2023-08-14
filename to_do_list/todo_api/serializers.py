from rest_framework import serializers
from app_todo.models import *

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"