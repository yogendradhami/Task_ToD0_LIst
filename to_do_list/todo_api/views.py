from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from app_todo.models import *
from .serializers import ToDoSerializer

from  rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import  User
# Create your views here.
# code for rest api



class CustomResponse():
    def successResponse(self, code, msg,  data=dict()):
        context = {
            'status_code': code,
            'message':msg,
            'data':data,
            'error':[]
                            }
        return context
    
    def  errorResponse(self, code, msg, error=dict()):
        context={
            'status_code':code,
            'message':msg,
            'error':error
        }

        return context
    
class ToDoViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=ToDoSerializer
    filter_backends=[DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields=('title','user','is_complete')
    search_fields=('title')
    ordering_fields=('is_complete','created_at','updated_at')

class ToDoApiView(APIView):
    def get(self, request):
        todo=Task.objects.all()
        serializer=ToDoSerializer(todo,many=True)
        return Response(CustomResponse.successResponse(200,"Task List", serializer.data), status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(CustomResponse.successResponse(200, "Added successfully",serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(CustomResponse.errorResponse(200, "Validation Error", serializer.errors))
        
class ToDoApiIdView(APIView):
    def get_object(self,id):
        try:
            data=Task.objects.get(id=id)
            return data
        except Task.DoesNotExist:
            return None
        
    def get(self,request,id):
        instance = self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=ToDoSerializer(instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
        
    def put(self,request,id):
        instance = self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer=ToDoSerializer(data=request,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


    def delete(self,request,id):
        instance=self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg":"Deleted successfully"}, status=status.HTTP_200_OK)


