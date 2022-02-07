# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path

#Importaciones de modelos
from loadImg.models import LoadImg

#IMportacion de serializers
from loadImg.serializers import LoadImgSerializers

class LoadImgTable(APIView):
    
    def get(self, request, format=None):
        queryset = LoadImg.objects.all()
        serializer = LoadImgSerializers(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "Archivo no seleccionado")
        archivos = request.data['url_img']
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = LoadImgSerializers(data=request.data)  
        if serializer.is_valid():
            validated_data = serializer.validated_data
            img = LoadImg(**validated_data)
            img.save()
            serializer_response = LoadImgSerializers(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoadImgTableDetail(APIView):
    def get_object(self, pk):
        try:
            return LoadImg.objects.get(pk = pk)
        except LoadImg.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        objetive = self.get_object(pk)
        if objetive != 0:
            objetive = LoadImgSerializers(objetive)
            return Response(objetive.data, status = status.HTTP_200_OK)
        return Response("No se encuentran datos ", status = status.HTTP_400_BAD_REQUEST)


    def put(self, request,pk, format=None):
        objetive = self.get_object(pk)
        archivos = request.data['url_img']
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = LoadImgSerializers(objetive, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objetive = self.get_object(pk)
        if objetive != 0:
            objetive.url_img.delete(save=True)
            objetive.delete()
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Dato introducido no encontrado en la base de datos",status = status.HTTP_400_BAD_REQUEST)