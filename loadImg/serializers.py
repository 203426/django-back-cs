from rest_framework import serializers

#Mandamos a traer los modelos
from loadImg.models import LoadImg

class LoadImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoadImg
        fields = ('pk','name_img','format_img', 'url_img')