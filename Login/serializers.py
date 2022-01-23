from rest_framework import serializers
from django.contrib.auth.models import User

# Creamos la clase usuario
class UserSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    
    # Se mandan los datos al modelo user predeterminado de python
    def create (self, validate_data):
        user=User()
        user.first_name=validate_data.get('first_name')
        user.last_name=validate_data.get('last_name')
        user.username=validate_data.get('username')
        user.email=validate_data.get('email')
        user.set_password(validate_data.get('password'))
        user.save()
        return user
    
    def validate_username(self,data):
        users=User.objects.filter(username=data)
        if len(users)!=0:
            raise serializers.ValidationError("Nombre ya existente, ingresar otro")
        else:
            return data