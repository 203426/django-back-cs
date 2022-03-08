# Create your views here.
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from rest_framework.permissions import IsAuthenticated

#Importaciones de modelos
from Profile.models import Profile
from django.contrib.auth.models import User


#IMportacion de serializers
from Profile.serializers import ProfileSerializer


class ProfileTable(APIView):
    permission_classes = [IsAuthenticated]
    
    def crearRes(self,user,data,status):
        jsonRes={
            "nombre":user[0]['first_name'],
            "apellido":user[0]['last_name'],
            "usuario":user[0]['username'],
            "email":user[0]['email'],
            "id_user":data.get('id_user'),
            "status":status
        }
        return json.loads(json.dumps(jsonRes))

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 404

    def get_object(self, idUser):
        try:
            return Profile.objects.get(id_user = idUser)
        except Profile.DoesNotExist:
            return 404

    def post(self, request):
        idUser = request.data['id_user']
        user = self.get_objectUser(idUser)
        requestData = request.data
        if(user != 404):
            
            serializer = ProfileSerializer(data=requestData)
            print(serializer.is_valid())
            if serializer.is_valid():
                # serializer.create(archivos,user)
                validated_data = serializer.validated_data
                
                profile = Profile(**validated_data)

                profile.save()

                serializer_response = ProfileSerializer(profile)

                return Response(serializer_response.data, status=status.HTTP_201_CREATED)    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message ":"El usuario no existe"})


    # def get(self, request,pk, format=None):
    #     print(pk)
    #     idResponse = self.get_object(pk)
    #     print(idResponse)
    #     if idResponse != 404:
    #         idResponse = ProfileSerializer(idResponse)
    #         user=User.objects.filter(id=pk).values()
    #         response=self.crearRes(user,idResponse.data,status.HTTP_200_OK)
    #         return Response(idResponse.data, status = status.HTTP_200_OK)
    #     return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        print(request.data)
        archivos = request.data['url_img']
        profileNew = self.get_object(request.data['id_user'])
        
        
        
        if(profileNew != 404):
            user=User.objects.filter(id=request.data['id_user'])
             
            print(User.objects.filter(id=request.data['id_user']).values())
            
            if(request.data['user']!=''):
                
                user.update(username=request.data['user'])
            
            if(request.data['email']!=''):
                
                user.update(email=request.data['email'])
            
            if(request.data['name']!=''):
                
                user.update(first_name=request.data['name'])
            
            if(request.data['apellido']!=''):
                
                user.update(last_name=request.data['apellido'])
                
                
            serializer = ProfileSerializer(profileNew,data=request.data)
            if serializer.is_valid():
                try:
                    os.remove('assets/'+str(profileNew.url_img))
                except os.error:
                    print("La imagen no existe")
                profileNew.url_img = archivos
                profileNew.save()
                return Response("Imagen actualizada", status=status.HTTP_201_CREATED)
            return Response("Error xd", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message ":"User doesn't exist"})

    # def delete(self, request):
    #     idUser = request.data['id_user']
    #     profile = self.get_object(idUser)
    #     if profile != 404:
    #         profile.url_img.delete(save=True)
    #         # profile.delete(save=True)
    #         return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
    #     return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)
    
class ProfileTableDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get_object(self, idUser):
        try:
            return Profile.objects.get(id_user = idUser)
        except Profile.DoesNotExist:
            return 404
        
    def crearRes(self,user,data,status):
        jsonRes={
            "nombre":user[0]['first_name'],
            "apellido":user[0]['last_name'],
            "usuario":user[0]['username'],
            "email":user[0]['email'],
            "id_user":data.get('id_user'),
            "img":data.get('url_img'),
            "status":status
        }
        return json.loads(json.dumps(jsonRes))
    
    def get(self, request,id_user, format=None):
        print(id_user)
        idResponse = self.get_object(id_user)
        print(idResponse)
        if idResponse != 404:
            idResponse = ProfileSerializer(idResponse)
            user=User.objects.filter(id=id_user).values()
            response=self.crearRes(user,idResponse.data,status.HTTP_200_OK)
            return Response(response)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
