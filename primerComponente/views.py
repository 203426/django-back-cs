from multiprocessing import context
from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# importaciones de modelos agregados
from primerComponente.models import PrimerTabla

# importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.
class PrimerTablaList(APIView):
    def get(self, request, format=None):
        queryset=PrimerTabla.objects.all()
        serializer=PrimerTablaSerializer(queryset,many=True ,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer=PrimerTablaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status=status.HTTP_201_CREATED )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class PrimerTablaDetail(APIView):
    def get_object(self,pk):
        try:
            return PrimerTabla.objects.get(pk=pk)
        except PrimerTabla.DoesNotExist:
            return "No existe"
        
    def get(self,request,pk,format=None):
        idResponse=self.get_object(pk)
        if idResponse != "No existe":
            idResponse=PrimerTablaSerializer(idResponse)
            return Response(idResponse.data,status=status.HTTP_200_OK)
        return Response("No hay dato",status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        idResponse=self.get_object(pk)
        serializer=PrimerTablaSerializer(idResponse,data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas=serializer.data
            return Response(datas,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Dato eliminado" ,status=status.HTTP_200_OK)
        else:
            return Response("Dato no encontrado",status=status.HTTP_400_BAD_REQUEST)