# Recursos de rest-framework
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status



from Profile.models import Profile
from django.contrib.auth.models import User
from Profile.serializers import ProfileSerializer


from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class LoginAuth(ObtainAuthToken):
    
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
    
    def post(self, request, *args, **kwargs):
        
        
        
        serializer=self.serializer_class(data=request.data,context={'request':request})
        
        # print(serializer)
        print(serializer.is_valid())
        
        if serializer.is_valid():
            user=serializer.validated_data['user']
            profile= self.get_object(user.pk)
            userObject=self.get_objectUser(user.pk)
            
            print(profile)
            # print(self.get_object(user).values())
            token,created=Token.objects.get_or_create(user=user)
            
            if profile!=404:
    
                return Response({
                    'token':token.key,
                    'user_id':user.pk,
                    'email':user.email,
                    'usuario':user.username,
                    'nombre':user.first_name,
                    'apellido':user.last_name,
                    'img':profile.url_img.name,
                    'id_img':profile.id,
                })
            else:
                return Response({
                    'token':token.key,
                    'user_id':user.pk,
                    'email':user.email,
                    'usuario':user.username,
                    'nombre':user.first_name,
                    'apellido':user.last_name,
                    'img':'img-profile/profile_unknow.png'
                })
        else:
            print('Que coño')
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    

# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (IsAuthenticated)
    # serializer_class = MyTokenObtainPairSerializer