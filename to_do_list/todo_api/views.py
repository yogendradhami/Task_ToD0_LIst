from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from app_todo.models import *
from .serializers import ToDoSerializer

# Create your views here.
# code for rest api
class ToDoViewSet(viewsets.ModelViewSet):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields=('title','user','is_complete')
    search_fields=('title')
    ordering_fields=('is_complete','created_at','updated_at')